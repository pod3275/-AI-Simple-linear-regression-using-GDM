# Simple-linear-regression-using-GDM
 - 2018년 1학기 성균관대학교 이지형 교수님 머신러닝 수업 1, 2번째 과제
 - 간단한 linear regression 문제

## 1. Problem
 - 다음 데이터를 최선으로 만족하는 모델을 제시하라.
 
   ![image](https://user-images.githubusercontent.com/26705935/40695408-0fcf755c-63fc-11e8-97e7-902ee2dd37b5.png)
   
   - Quadratic model을 universal model로 사용하라.
   
     ![image](https://user-images.githubusercontent.com/26705935/40695442-373f1264-63fc-11e8-8482-c16c987c690a.png)
     
   - Error function은 다음과 같은 MSE를 사용하라.
   
     ![image](https://user-images.githubusercontent.com/26705935/40695566-b60bc47a-63fc-11e8-9671-ec6fa00b3b48.png)
     
   - Update 방식으로 Gradient Descent Method를 사용하라.
   
     ![image](https://user-images.githubusercontent.com/26705935/40695750-870bde5c-63fd-11e8-880e-56db325f365f.png)

    
## 2. Environment
 - language : python 3.6
 - IDE : JetBrains PyCharm Community Edition 2017.3.2
 
## 3. Result
 - 주어진 데이터, universal function으로 총 error를 계산한다.
 
   ![image](https://user-images.githubusercontent.com/26705935/40695651-1cc5c54e-63fd-11e8-8907-30909e91992c.png)
 
 - 파라미터인 w0, w1, w2에 대해 미분한 식을 구한다.
 
   ![image](https://user-images.githubusercontent.com/26705935/40695704-525a79fc-63fd-11e8-84d2-a16bba85cf1c.png)
   
 - Gradient Descent Method 식에 미분 식을 적용하여, 파라미터를 update한다.
 
 - 결과
   - 파라미터의 initial point는 random 설정.
   - n = learning rate = 0.5로 설정.
   - 첫 번째  
     ![image](https://user-images.githubusercontent.com/26705935/40695836-010d8cdc-63fe-11e8-93c3-7547e7520e7f.png)
     
   - 두 번째   
     ![image](https://user-images.githubusercontent.com/26705935/40695867-2d2f1db2-63fe-11e8-879a-52067e16241a.png)
     
   - 세 번째  
     ![image](https://user-images.githubusercontent.com/26705935/40695892-448352b2-63fe-11e8-961b-5d840f170907.png)
  
 ## 4. Future work
 - 미분 식을 직접 계산하지 않고, GDM을 적용하는 라이브러리를 이용하여 구현해보기.
