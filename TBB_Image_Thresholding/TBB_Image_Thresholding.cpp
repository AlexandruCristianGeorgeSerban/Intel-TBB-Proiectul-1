// TBB_Image_Thresholding.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <opencv2/opencv.hpp>
#include <opencv2/core/utils/logger.hpp>

#include <iostream>
#include <filesystem>
#include <vector>
#include <chrono>
#include <string>

using namespace std;

namespace fs = filesystem;

vector<string> getImagePaths(const string& folderPath)
{
    vector<string> imagePaths;

    for (const auto& entry : fs::directory_iterator(folderPath))
    {
        if (entry.is_regular_file())
        {
            string extension = entry.path().extension().string();

            if (extension == ".jpg" || extension == ".jpeg" ||
                extension == ".png" || extension == ".bmp")
            {
                imagePaths.push_back(entry.path().string());
            }
        }
    }

    return imagePaths;
}

void processImageSequential(const string& inputPath, const string& outputFolder)
{
    cv::Mat image = cv::imread(inputPath);

    if (image.empty())
    {
        cout << "Could not read image: " << inputPath << endl;
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
    string outputPath = outputFolder + "/" + inputFile.stem().string() + "_binary.png";

    cv::imwrite(outputPath, binary);
}

int main()
{
    cv::utils::logging::setLogLevel(cv::utils::logging::LOG_LEVEL_WARNING);

    string inputFolder = "dataset";
    string outputFolder = "output_sequential";

    fs::create_directories(outputFolder);

    vector<string> imagePaths = getImagePaths(inputFolder);

    if (imagePaths.empty())
    {
        cout << "No images found in folder: " << inputFolder << endl;
        return 1;
    }

    cout << "Found " << imagePaths.size() << " images." << endl;

    auto start = chrono::high_resolution_clock::now();

    for (const auto& imagePath : imagePaths)
    {
        processImageSequential(imagePath, outputFolder);
    }

    auto end = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed = end - start;

    double totalTime = elapsed.count();
    double throughput = imagePaths.size() / totalTime;

    cout << "\nSequential processing finished." << endl;
    cout << "Total time: " << totalTime << " seconds" << endl;
    cout << "Throughput: " << throughput << " images/second" << endl;

    return 0;
}
