---
title: "Interpolation Curve Fitting Part 4 Bilinear Interpolation 2D"
source: "https://www.youtube.com/watch?v=va8vFViss90"
author:
  - "[[Engineering Mathematic I]]"
published: 2020-05-18
created: 2026-10-24
description: "在 YouTube 上畅享你喜爱的视频和音乐，上传原创内容并与亲朋好友和全世界观众分享你的视频。"
tags:
  - "clippings"
---

> 对应笔记：[[双线性插值 从一维线性到二维图像]]

![](https://www.youtube.com/watch?v=va8vFViss90)

## Transcript

### Introduction to 1d interpolation

**0:00** · previously you have learned how to perform the linear interpolation in 1d for example if these two points are given we are going to predict the interpolated data between the x axis this can be done by using the 1d linear interpolation for example for the 0.1 and 0.2 given here given the x i between the x1 and x2 here

**0:26** · we are going to find and interpolate the function at x i here if the function is also given here in the y direction then your function is no longer 1d which is in the x direction but in 2d in xy direction for the first point you have x1 y1 which is located over here and the function for x1 y1 is this value

### Concept of bilinear interpolation

**0:58** · for the second point you have x2 y1 which is located over here and the function for the x2 y1 is this value the point is located at the x1 y2 which is here and this is the function

**1:15** · at x1 y2 for the last point you have x2 y2 which is located here and this is the function for the x2y2 if these four points are given you are going to predict the function in between this plane which is between y1 to y2 and x1 to x2 so you are going to interpolate the function at x i y i which is located at this plane

**1:47** · in this case we can use the bilinear interpolation to solve the 2d interpolation problem here to perform the bilinear interpolation in the first step let's interpolate in the x direction and assume a constant y one based on the function given at point one and point two here where

### Deriving the bilinear formula

**2:09** · in this direction the y1 is constant it changed from x1 to x2 then by using these two points we can use the linear interpolation which is stored in the equation 1a to find the function at x i here and y1 so this is the point that

**2:29** · you want to interpolate and this point is between x1 to x2 in the step 1b you continue the interpolation in the x direction where you assume the constant y2 in this direction your y2 is constant and then you interpolate from the x1 to x2 0.3 and 0.4 are given which is located at x1 and x2 which is this point and x2

**2:58** · y2 which is this point so the function at these two points are given and then you are going to interpolate the function at x i where your x i is between x1 to x2 and at constant y2 which is this point this can be obtained by using the linear interpolation formula from step 1 a and step 1b you should be able to obtain the function as x i y 1 and y 2 which is located at these two pawns now

**3:32** · we take the x i to be constant and then we interpolate from the y1 to y2 by using these two points we can use the equation two which is the linear interpolation to find the f x i y i at this point we have four given point here and in graph you can draw this point at

### Generalizing the formula

**3:58** · here and you want to interpolate the f x i y i where your x i is from this point to this point and your y i is from this point to this point so you form a plane so this plane is the function that you want to interpolate previously you perform two linear interpolation in the x direction here

**4:28** · to obtain the equation 1a and 1b then you perform linear interpolation in the y direction here to find the equation 2. in the step 3 you need to substitute the equation 1a and 1b which is these two into the equation 2.

**4:50** · after you substitute the equation 1a into the equation 2 here you obtain this component and then substitute the equation 1b into the component here you obtain this component this equation is called the bilinear interpolation that can be used to find the f x i y i which is located between these four points in this example you have a rectangular heated plate where the temperature at least four points are given

### Example: heated plate

**5:22** · the coordinate of the plane is given as well so at this point you have x at this point you have y so this is your x axis because your x is changing and then this is your y axis because your y is change from one

**5:40** · to six then let's assume this to be our first point and we extract the information for first point where you have the x equal to two y equal to 1 and the temperature function f x y is equal to 16. for the first pawn you have x1 and y1 so let's move to this point

**6:03** · we have point 2 where your y1 is constant which is 1 then you have the x 2 change to 9. with that you obtain the information for your 0.2 and the function is equal to 57.5 degree celsius you continue with the 0.3 here

**6:31** · where you can see the x1 remain the same to be 2 so this is your x1 here and your y 1 change to y 2 from 1 to 6 and the temperature function here is 55

**6:51** · so for the last point here so you have the x2 and y2 which is these two points and the temperature is 70 degree celsius so these four points are given we are going to interpolate the temperature within this four pawn which is this plane

**7:13** · so let's say we take a point from this plane this point is in the coordinate x i and y i and we want to find the temperature at this x i y i we can use the bilinear interpolation to solve the 2d interpolation problem here if i substitute all of the information given by this four point into this formula then you can simplify

### Calculating temperature distribution

**7:38** · the formula into this and this function is in terms of the x i and y i where your x i is between this point two and nine and your y i is between one year to 6

**8:01** · if you want to find the temperature at this point which is the temperature at 0.7 in the x axis 5 in the y axis then in this case your x i is equal to 7 and y i equal to 5 substitute inside the formula and compute you should obtain this answer to find the temperature distribution within these four points then separate and split these into hundred point one two three four and so on

**8:33** · until hundred and in the y-axis it will also split into one 2 3 4 until 100 here with that you obtain 100 times 100 which is equal to

**8:50** · 10 000 temperature with that you obtain 100 times 100 which is equal to 10 000 points on this plane substitute all of this point into this formula then you can obtain the temperature at this 10 000 points it's impractical for us to manually calculate it by hand so we should use computer to do this so

### Matlab implementation and visualization

**9:14** · this is the programming by using the matlab so first of all you split the x from 0.2 to 0.9 here and split it into 100 points then you split the y from 1 to 6 into 100 point as well

**9:35** · then you perform the math grid to combine the x and y coordinates into a matrix here by substitute the x y coordinate into the bi-linear interpolation formula here then you can find the temperature at this point then you can perform the surface plot where you have the x y coordinate as well as the temperature so this is the x coordinate from 2 to 9

**10:02** · and this is the y y-coordinate from 1 to 6 and then the height is the temperature by looking at this 3-d graph in the top view then you obtain this block so this is the temperature distribution that you obtain where you can see the red color means the temperature is high and the blue color here means that you

**10:27** · have a lower temperature you should know now how to perform the bilinear interpolation to find the temperature distribution within four form