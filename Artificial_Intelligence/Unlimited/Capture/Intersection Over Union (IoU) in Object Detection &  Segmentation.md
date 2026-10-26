---
title: "Intersection Over Union (IoU) in Object Detection &  Segmentation"
source: "https://www.youtube.com/watch?v=RgQbweTwrkU"
author:
  - "[[LearnOpenCV]]"
published: 2023-07-31
created: 2026-10-24
description: "📚 Blog post Link: https://learnopencv.com/fine-tuning-trocr-training-trocr-to-recognize-curved-text/📚 Check out our FREE Courses at OpenCV University : https://opencv.org/university/free-courses/"
tags:
  - "clippings"
---

> 对应笔记：[[IoU 交并比 检测与分割的评价指标]]

![](https://www.youtube.com/watch?v=RgQbweTwrkU)

📚 Blog post Link: https://learnopencv.com/fine-tuning-trocr-training-trocr-to-recognize-curved-text/  
📚 Check out our FREE Courses at OpenCV University : https://opencv.org/university/free-courses/  
  
Dive into the world of Object Detection and Segmentation with our exploration of Intersection Over Union (IoU), an essential metric that quantifies the overlap between prediction and ground truth. Whether you're a computer vision professional or an enthusiast, understanding IoU is crucial in evaluating a model's accuracy. Join us as we break down this vital checkpoint in an easy-to-understand format.  
  
Topics Covered  
  
✅ Intersection over Union in Object Detection  
✅ Intersection over Union in Image Segmentation  
✅ Implementing IoU using NumPy  
✅ Implementing IoU using PyTorch  
  
⭐️ Time Stamps:⭐️  
00:00-00:12: Introduction  
00:12-00:31: Object Detection  
00:31-02:00: IOU  
02:00-02:59: IOU for Object Detection  
02:59-06:32: IOU for Segmentation  
06:32-06:54: Outro  
  
Resources:  
🖥️ On our blog - https://learnopencv.com we also share tutorials and code on topics like Image  
Processing, Image Classification, Object Detection, Face Detection, Face Recognition, YOLO, Segmentation, Pose Estimation, and many more using OpenCV(Python/C++), PyTorch, and TensorFlow.  
  
🤖 Learn from the experts on AI: Computer Vision and AI Courses  
YOU have an opportunity to join the over 5300+ (and counting) researchers, engineers, and students that have benefited from these courses and take your knowledge of computer vision, AI, and deep learning to the next level.🤖  
https://opencv.org/courses  
  
#️⃣ Connect with Us #️⃣  
📝 Linkedin: https://www.linkedin.com/in/satyamallick/  
📱 Twitter: https://twitter.com/LearnOpenCV  
🔊 Facebook: https://www.facebook.com/profile.php?id=100064001437329  
📸 Instagram: https://www.instagram.com/learnopencv/  
🔗 Reddit: https://www.reddit.com/user/spmallick  
  
🔖Hashtags🔖  
#ObjectDetection #ImageSegmentation #IntersectionOverUnion #IoU #ComputerVision #PyTorch #ModelAccuracy#MachineLearning #ArtificialIntelligence #DeepLearning #AI #opencvunibersity #deeplearning #computervision #learnopencv #opencv

## Transcript

### Introduction

**0:02** · All right, let's get this started! Object Detection plays a vital role in a wide range of applications from Autonomous Driving Systems to Surveillance cameras identifying potential threats. There needs to be a metric to evaluate the quality of bounding boxes after detection. That's where Intersection over Union or IOU comes into picture. It can be mathematically expressed as Area of Intersection over Area of Union. Let's use this bird image as a reference. We have three object detection models, model A, Model B and model C.

### Object Detection

### IOU

**0:38** · Ground Truth has been Illustrated using red color and predictions are shown using cyan color. model A has a relatively higher overlap with the Ground Truth compared to model B. We might conclude that model A is performing better right but hold on, there's more to the story! Model C comes into the picture, it has an even higher overlap with the Ground Truth than model B. In model C we can observe that the localization of prediction is even higher where even the branch of the tree is included. Here's an introduction to IOU.

**1:13** · It's the ratio of the overlap area to the combined area of prediction and Ground Truth. The numerator will be lesser as the prediction fails to predict the area inside the Ground Truth. if the area of predicted box is higher, then the denominator will also be higher making the IOU lower.

**1:39** · It is expressed as a value between 0 or 1, where 0 indicates no overlap and one indicates a perfect match or a complete overlap. Now we will explore IOU for Object Detection and Segmentation. Let's discuss IOU for Object Detection first. In object detection IOU is a helper metric when compared to other metrics such as Recall, Loss or Map. To understand this, let's look closely at three different predictions. There are two main parameters, the IOU threshold represented by alpha and the IOU value calculated individually for each prediction.

### IOU for Object Detection

**2:13** · Now we will compare the IOU threshold with the IOU values. The first prediction is a true positive because IOU which is 0.96, is greater than the IOU threshold which is 0.5. If we set the Threshold at 0.97, it becomes a false positive. Similarly the second prediction shown on how is a false positive due to the threshold. Theoretically, the third prediction can also be a true positive given that we lower the threshold all the way to zero. Let's move on to IOU for Segmentation.

**2:46** · It serves as a primary metric to evaluate model accuracy. Have a look at the visualization shown on screen.

### IOU for Segmentation

**2:59** · In the case of Image Segmentation, the area is not necessarily rectangular, it can have any regular or irregular shape. That means the predictions are segmentation masks and not bounding boxes. Pixel by pixel analysis is done, moreover the definition of true positive false positive and false negative is slightly different as it is not based on a predefined threshold. Let's quickly hop on to a Google Collab notebook. PyTorch has an inbuilt functionality that allows it to compute IOU values.

**3:36** · Initially the necessary packages such as PyTorch and Torch Vision are imported. In the next cell the coordinates for both the Ground Truth and prediction bounding boxes are defined.

**3:49** · From here the IOU metric can simply be calculated by using the ops dot box underscore IOU function and pass both the predefined bounding box coordinates to it.

**4:02** · In the end, the computed IOU value can be printed. To get a much more clear understanding of what happens within this predefined function, let's look at two different explanations.

**4:17** · In the diagram shown on screen, we can observe two overlapping bounding boxes.

**4:22** · One of them is the Ground Truth represented by A1 and the other is the prediction represented by A2.

**4:31** · Area of intersection is the intersection of A1 and A2. The union can be expressed as A1 plus A2 minus area of intersection. The basic idea here is to compute area of intersection. We do know that both the bounding boxes are overlapping the top left corner of the bounding box is represented by x min and y min whereas the bottom right corner of the bounding box is represented by x max and y max. So x-min y min x max and y max can be calculated using the expressions shown on screen.

**5:12** · Let's look into another example. In this visualization, we can observe that the bounding boxes are not overlapping. In this case, we just need to calculate the height and the width to calculate the area of intersection. The height of the intersection is calculated by subtracting y2 min from y1 max. This subtraction gives us the vertical distance between the top and bottom edges of the intersection. Similarly the width of the intersection is computed by subtracting x2 min from x1 max.

**5:43** · This subtraction yields the horizontal distance between the left and right edges of the intersection. However, to ensure that the height and width are always a positive value, we take the maximum of the result and 0. This prevents negative values from being considered as the height or width. This solves our specific purpose as either the height or width might be zero and hence the area of intersection is also zero.

**6:07** · The same concept has been applied using Python in the manual approach for IOU calculation shown on this Google Collab notebook and that's a wrap for today's video. Make sure to LIKE and SUBSCRIBE to our Channel for more exciting Computer Vision content. If you have any questions or suggestions, please feel free to leave them in the COMMENTS down below. If you like this video, why don't you check out our YOLO Master Class, Master the Vision playlist. Thanks for watching and I'll see you in the next video!