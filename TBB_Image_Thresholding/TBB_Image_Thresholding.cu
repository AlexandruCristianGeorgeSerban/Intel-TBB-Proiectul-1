// TBB_Image_Thresholding.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <opencv2/opencv.hpp>
#include <opencv2/core/utils/logger.hpp>
#include <cuda_runtime.h>
#include <device_launch_parameters.h>

#include <iostream>
#include <filesystem>
#include <vector>
#include <chrono>
#include <string>

using namespace std;
namespace fs = filesystem;

__global__ void adaptiveThresholdKernel(const unsigned char* input, unsigned char* output,
    int width, int height, int windowSize, int C)
{
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;

    if (x < width && y < height)
    {
        int halfWindow = windowSize / 2;
        int sum = 0;
        int count = 0;

        for (int dy = -halfWindow; dy <= halfWindow; dy++)
        {
            for (int dx = -halfWindow; dx <= halfWindow; dx++)
            {
                int ny = y + dy;
                int nx = x + dx;

                ny = max(0, min(ny, height - 1));
                nx = max(0, min(nx, width - 1));

                sum += input[ny * width + nx];
                count++;
            }
        }

        int mean = sum / count;
        unsigned char pixelValue = input[y * width + x];

        if (pixelValue > (mean - C)) {
            output[y * width + x] = 255;
        }
        else {
            output[y * width + x] = 0;
        }
    }
}

vector<string> getImagePaths(const string& folderPath)
{
    vector<string> imagePaths;
    for (const auto& entry : fs::directory_iterator(folderPath)) {
        if (entry.is_regular_file()) {
            string ext = entry.path().extension().string();
            if (ext == ".jpg" || ext == ".jpeg" || ext == ".png" || ext == ".bmp") {
                imagePaths.push_back(entry.path().string());
            }
        }
    }
    return imagePaths;
}

void processImageCUDA(const string& inputPath, const string& outputFolder)
{
    cv::Mat image = cv::imread(inputPath);
    if (image.empty()) return;

    cv::Mat gray;
    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);

    int width = gray.cols;
    int height = gray.rows;
    size_t mem_size = width * height * sizeof(unsigned char);

    cv::Mat binary(height, width, CV_8UC1);

    unsigned char* d_input, * d_output;
    cudaMalloc(&d_input, mem_size);
    cudaMalloc(&d_output, mem_size);

    cudaMemcpy(d_input, gray.data, mem_size, cudaMemcpyHostToDevice);

    dim3 threadsPerBlock(16, 16);
    dim3 numBlocks((width + threadsPerBlock.x - 1) / threadsPerBlock.x,
        (height + threadsPerBlock.y - 1) / threadsPerBlock.y);

    adaptiveThresholdKernel <<<numBlocks, threadsPerBlock >>> (d_input, d_output, width, height, 15, 5);

    cudaDeviceSynchronize();

    cudaMemcpy(binary.data, d_output, mem_size, cudaMemcpyDeviceToHost);

    cudaFree(d_input);
    cudaFree(d_output);

    fs::path inputFile(inputPath);
    string outputPath = outputFolder + "/" + inputFile.stem().string() + "_cuda.png";
    cv::imwrite(outputPath, binary);
}

int main()
{
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_WARNING);

    string inputFolder = "dataset";
    string outputFolder = "output_cuda";

    fs::create_directories(outputFolder);
    vector<string> imagePaths = getImagePaths(inputFolder);

    if (imagePaths.empty()) {
        cout << "No images found in folder: " << inputFolder << endl;
        return 1;
    }

    int gpuThreadsPerBlock = 16;

    cout << "Found " << imagePaths.size() << " images." << endl;
    cout << "Starting CUDA processing on the GPU..." << endl;
    cout << "Using blocks of " << gpuThreadsPerBlock << "x" << gpuThreadsPerBlock << " GPU threads." << endl;

    auto start = chrono::high_resolution_clock::now();

    for (const auto& imagePath : imagePaths)
    {
        processImageCUDA(imagePath, outputFolder);
    }

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed = end - start;
    double totalTime = elapsed.count();
    double throughput = imagePaths.size() / totalTime;

    cout << "\nCUDA processing finished." << endl;
    cout << "Total time: " << totalTime << " seconds" << endl;
    cout << "Throughput: " << throughput << " images/second" << endl;

    return 0;
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file