# 아키텍처는 왜 중요한가?

"난 나만의 아키텍처를 설계하고 개발할거야! 히히" 라는 생각을 가진 개발자가 있어서
같이 협업을 진행하다고 가정해보자. 그러면 아래와 같은 문제점이 발생할 것 이다.

1. 나만 읽기 좋은 아키텍처는 남이 읽는데 굉장한 시간이 걸린다.
2. IT 직군은 시간 == 돈(비용)이다.
3. 협업하는 팀원이 하나의 요구사항을 받아서 기능을 추가하기 까지 굉장한 시간이 걸린다.

좋은 아키텍처(잘 설계한 아키텍처)를 설계하고 팀원과 협업을 진행한다면,
남이 읽기 좋은 코드가 되어있을 것이고, 하나의 요구사항을 받아서 기능을 추가하기까지 시간이 빨라진다.

![image](https://user-images.githubusercontent.com/82089918/235816389-1c3de5c5-b5ba-44e4-b92e-2472e4f82300.png)

<br>

# 계층형 아키텍처의 단점

## 1. 계층간 구분이 모호함

![image](https://user-images.githubusercontent.com/82089918/235816927-b25248b5-30e6-46af-be1b-67834f8475c6.png)

계층형 아키텍처로 프로젝트를 개발하다 보면 컨트롤러에서 엔티티를 접근해서 개발을 해볼까라는 생각이 든적이 있을것이다. 
이렇게 된다면 테스트 코드를 작성하기에 굉장히 어려워질 것이고, 핵심 도메인(비지니스 로직)이 컨트롤러 계층에 몰려있어서 계층이 **짬뽕**이 될것이다. 

<br>

## 2. 의존성 결합

이것은 모 개발자가 개발한 프로젝트 코드를 가져온것이다.

<img width="736" alt="image" src="https://user-images.githubusercontent.com/82089918/235818465-28e1f293-ad8b-48ca-9a5c-b25d7f485c13.png">

<img width="690" alt="image" src="https://user-images.githubusercontent.com/82089918/235818535-ea21f6d7-beea-42dc-a464-41ad5e05fb2f.png">

<img width="532" alt="image" src="https://user-images.githubusercontent.com/82089918/235818566-16801ac4-c921-42b8-9724-e6822e5b3080.png">

presentation 계층에 있는 dto가 controller, service까지 의존하고 있다.
이렇게 되면 presentaion인 dto를 변경하게 된다면 service의 코드까지 변경해야 한다는 불상사가 생긴다.

<br>

# 클린 아키텍처는 뭔데?

클린 아키텍처는 기존의 계층형 아키텍처에서 가지는 의존성에서 벗어나도록 하는 아키텍처이다.

![image](https://user-images.githubusercontent.com/82089918/235816679-77080354-0467-4d5b-a28e-269efe735318.png)

![image](https://user-images.githubusercontent.com/82089918/235836779-e70d6f93-1871-4772-8f86-fb24aed92cd6.png)

위 사진을 보면 시스템을 구성하는 영역을 4개로 나눈것이다. <br>
의존성은 가장 밖에서 안으로 흘러야한다. 안에서 밖으로 흐르는것은 안된다.

### 1. Entity

- 핵심 업무 규칙(비지니스 규칙)을 캡슐화 한것이다.
- 메서드를 가지는 객체, 일련의 데이터 구조와 함수의 집합이다.
- 가장 변하지 않으며, 외부로부터 영향을 받지 않는 영역이다.

### 2. UseCase
- 애플리케이션의 특화된 업부 규칙을 포함한다.
- 즉, 사용자 또는 시스템이 수행하는 작업 또는 시나리오를 나타낸다.
- Entity로 들어오고 나가는 데이터 흐름을 조정하고 조작한다.

### 3. Inrerface Adapter
- 컨트롤러, 프레젠터, 게이트웨이 등이 여기에 속한다.
- 데이터 형식을 애플리케이션이 알아먹을 수 있게 변환한다.

### 4. Infrastructure
- UI, DB, Frameworks, Devices등이 있는 영역이다.
- 변화 가능성이 가장 높기 때문에 Entity와 확실히 분리되어야 한다.

<br>

# 마무리

내가 개발한 클린 아키텍처 코드

https://github.com/team-goms/GOMS-Backend