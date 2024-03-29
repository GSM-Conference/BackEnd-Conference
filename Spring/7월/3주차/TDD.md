# TDD

### 테스트코드를 작성해야 하는 이유
+ 검증하기가 쉽고, 신뢰성이 높다.
+ 리펙토링 시에 안정성을 확보할 수 있다.
+ 테스트에 진행되는 시간을 절약할 수 있다.

### 좋은 테스트 코드를 위한 'FIRST 규칙'
+ Fast : 테스트는 빠르게 동작해야한다.
+ Independent : 테스트는 서로 의존하면 안된다.
+ Repeatable : 어느 환경에서도 반복되야 한다.
+ Self-Validating : 테스트에 대한 결과는 자체적으로 검증되어야 한다.
+ Timely : 테스트코드는 실제 코드를 작성하기 전에 작성해야 한다.

### TDD 개발 방식
TDD(Test-Driven Development)는 소프트웨어 개발방법론 중 하나이다.<br>
TDD와 일반적인 개발 방식의 차이점은 일반적인 개발은 실제 코드를 다 짜고 테스트코드를 짜지만 TDD에서는 테스트코드를 먼저 짜고 실제코드를 짜는 방식이다.<br>
테스트코드를 짜면서 기능에서 발생하는 예외나 수정사항등을 설계하면서 프로그램을 개선시킨다.<br>
이후에는 테스트코드에 맞게 테스트코드를 통과할 수 있는 실제 코드를 짠다.

### 절차
![img](https://media.fastcampus.co.kr/wp-content/uploads/2021/03/tdd_img_3-1030x558.png)

+ Red 단계에서는 실패하는 테스트코드를 작성한다.
+ Green 단계에서는 성공하는 테스트코드를 작성한다.
+ Blue 단계에서는 코드를 리펙토링한다.

### TDD를 사용해야 하는 이유
1. 디버깅 시간을 줄일 수 있다.
2. 가장 빠르게 피드백 가능
    + 개발자가 테스트를 할 때는 대부분 `인수테스트`로 테스트를 한다. 인수테스트로 테스트를 하면 문제를 발견해도, 정확하게 뭐가 문제인지 모를수도 있다.
    + TDD는 기능별로 테스트를 진행하기 때문에 코드가 개발자의 손을 떠나기 전에 피드백을 한 번 더 받을 수 있다.
3. 재설계 시간을 단축 할 수 있다.
    + 테스트 시나리오를 짜면서 다양한 예외사항에 대해 생각해볼 수 있다. 이는 소프트웨어의 전반적인 설계가 변경되는 일을 방지할 수 있다.

### 단점
1. 생산성 저하
    + 개발 속도가 느려진다. 왜냐하면 처음부터 하나의 기능에 2개의 코드를 짜야하기 때문에 TDD 방식의 개발은 기존의 개발보다 10~30% 정도로 늘어난다.<br>
    + SI 프로젝트에서는 소프트웨어의 품질보다 납기일 준수가 훨씬 중요하기 때문에 TDD 방식을 잘 사용하지 않는다

### 마무리
TDD를 시도해볼만 할 때
+ 내/외부적으로 불확실성이 높은 경우
    + 내부적 요소: 처음 해보는 프로젝트, 생소한 기술들
    + 외부적 요소: “이거 변경해주세요” “다른 기능도 추가해주세요”

+ 코드를 많이 수정해야 하는 경우
+ 나중에 다른 누군가가 개발해야 하는 경우

큰 규모의 시스템을 운영할 프로젝트에서 개발자들이 TDD를 통해 초기에 많은 문제를 잡고, 그 문제를 해결하면서 더 좋은 애플리케이션을 설계할 수 있다는 점에서는 TDD는 좋은 거 같습니다.<br>

