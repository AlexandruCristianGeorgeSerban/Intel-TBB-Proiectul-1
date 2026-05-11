// TBB_Image_Thresholding.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <opencv2/opencv.hpp>

#include <iostream>
#include <filesystem>
#include <vector>
#include <chrono>
#include <string>

namespace fs = std::filesystem;

std::vector<std::string> getImagePaths(const std::string& folderPath)
{
    std::vector<std::string> imagePaths;

    for (const auto& entry : fs::directory_iterator(folderPath))
    {
        if (entry.is_regular_file())
        {
            std::string extension = entry.path().extension().string();

            if (extension == ".jpg" || extension == ".jpeg" ||
                extension == ".png" || extension == ".bmp")
            {
                imagePaths.push_back(entry.path().string());
            }
        }
    }

    return imagePaths;
}

void processImageSequential(const std::string& inputPath, const std::string& outputFolder)
{
    cv::Mat image = cv::imread(inputPath);

    if (image.empty())
    {
        std::cout << "Could not read image: " << inputPath << std::endl;
        return;
    }

    cv::Mat gray;
    cv::cvtColor(image, gray, cv::COLOR_BGR2GRAY);
        
    cv::Mat binary;
    cv::adaptiveThreshold(
        gray,
        binary,
        255,
        cv::ADAPTIVE_THRESH_GAUSSIAN_C,
        cv::THRESH_BINARY,
        15,
        5
    );

    fs::path inputFile(inputPath);
    std::string outputPath = outputFolder + "/" + inputFile.stem().string() + "_binary.png";

    cv::imwrite(outputPath, binary);
}

int main()
{
    std::string inputFolder = "dataset";
    std::string outputFolder = "output_sequential";

    fs::create_directories(outputFolder);

    std::vector<std::string> imagePaths = getImagePaths(inputFolder);

    if (imagePaths.empty())
    {
        std::cout << "No images found in folder: " << inputFolder << std::endl;
        return 1;
    }

    std::cout << "Found " << imagePaths.size() << " images." << std::endl;

    auto start = std::chrono::high_resolution_clock::now();

    for (const auto& imagePath : imagePaths)
    {
        processImageSequential(imagePath, outputFolder);
    }

    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> elapsed = end - start;

    double totalTime = elapsed.count();
    double throughput = imagePaths.size() / totalTime;

    std::cout << "\nSequential processing finished." << std::endl;
    std::cout << "Total time: " << totalTime << " seconds" << std::endl;
    std::cout << "Throughput: " << throughput << " images/second" << std::endl;

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
