# Blink

![image](https://user-images.githubusercontent.com/57009810/161487103-9108dc4d-cc7f-4bd6-992c-d7918c8d7da7.png)

_A horror-movie-inspired eye tracking program that changes pictures by detecting blinking and gaze direction._

-----------

<h2>Project Details:</h2>

**Dev Tools:** OpenCV, Dlib

**Programming Language:** Python

<h2>Build Process</h2>

<h3>Landmarks</h3>

![landmarks_points](https://user-images.githubusercontent.com/57009810/161487421-bb91abc8-5289-469c-ae99-57a83eee3513.png)

- Used Dlib to track landmarks on face

<h3>Tracking the Eyes</h3>

![image](https://user-images.githubusercontent.com/57009810/161487991-3b030776-8553-4314-b39c-94caadfbbe66.png)

- Used OpenCV and Dlib to track the eyes

<h3>Image Sequence</h3>

<h4>Image 1: Lights Off</h4>

![image](https://user-images.githubusercontent.com/57009810/161488477-b3565f02-c217-4a80-9665-576ffb482d84.png)

<h4>Image 2: Lights On</h4>

![image](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2ef2be9d-f4ca-4552-8ac3-71d53f66fe94/playtest2.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220404T064915Z&X-Amz-Expires=86400&X-Amz-Signature=3dd5041acfaafd9673112e52d6dfa737ff0d67066a411c6d53e144623a0efc1e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22playtest2.jpg%22&x-id=GetObject)

<h4>Image 3: Figure Appears</h4>

![image](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a77b23d4-0c71-4d81-928c-f3f4cdced2b5/playtest3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220404T064917Z&X-Amz-Expires=86400&X-Amz-Signature=7fc14d5bb4c03f889872e8144e7cf2c89b51dd0750ad175ba2455452fbbc63b6&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22playtest3.jpg%22&x-id=GetObject)

<h3>Eye Tracking</h3>

<h4>Centered Gaze</h4>

![image](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d0dceef4-f167-4494-8522-d5f7d817cdcb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220404T065136Z&X-Amz-Expires=86400&X-Amz-Signature=02d5ab83cfc11fab254ab66ba08f29217b8af79d3bc82ad52df812b965e8f219&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

<h4>Gaze Offscreen: Left & Right</h4>

![image](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/656e8c7f-0906-4fe7-b0d5-b915cd50fd24/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220404T065139Z&X-Amz-Expires=86400&X-Amz-Signature=f15b353e1612719bd5237df9a56a3eff4a02b28df76c19d172b77ca9ff62605d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

![image](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f0d9ca1a-37e4-46e9-a740-91fddfc0321f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220404T065141Z&X-Amz-Expires=86400&X-Amz-Signature=a40651191b1cc11e51d03469809a0864d267196077262dba380fbdd43d8b073e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

<h4>Blink</h4>

![image](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/52fc607b-1503-4482-8d28-d31180a5cde5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220404T065143Z&X-Amz-Expires=86400&X-Amz-Signature=88fed122013f756ee1d07953eb953def49082c714e02f54ff89710d8229b23e8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)

<h3>Program Logic Flow Chart</h3>

![image](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a6d0b34d-d5dd-4867-8f08-41e988055325/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20220404%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20220404T065116Z&X-Amz-Expires=86400&X-Amz-Signature=6e5f80e9e2720ef5bec332f325c395347388c63f65a73a3ba4a3ff89d658ac16&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22&x-id=GetObject)
