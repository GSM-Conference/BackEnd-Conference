## **CI(Continuous Integration)**

CI(Continuous Integration)는 지속적인 통합이라는 의미이다.   
애플리케이션의 버그 수정이나 새로운 코드 변경이 주기적으로 빌드 및 테스트되면서 공유되는 레파지토리에 통합(merge)되는 것을 의미한다.   
따라서 여러 명의 개발자가 동시에 애플리케이션 개발과 관련된 코드 작업을 할 경우 서로 충돌하는 문제를 이 방법으로 해결할 수 있다.

<br>

## **GitHub Action**

Github에서 제공되는 CI/CD 플랫폼이다. Pull Request가 생성되면 해당 코드에 대한 테스트와 빌드를 자동으로 실행하거나, Merge된 PR에 대한 배포를 자동화할 수 있다. 이런 DevOps 작업을 넘어, 단순히 Issue가 생성되었을 때 적절한 label을 등록하는 등의 단순한 워크플로우도 작성해볼 수 있다.

## **GitHub Actions 구성 요소**

![image](https://hudi.blog/static/25fea31e38a998447f0ece2340bc519d/9d567/github-actions-components.png)

<br>

### **워크플로우(workflow)**

하나 이상의 작업이 실행되는 자동화 프로세스이다. 워크플로우가 언제 트리거될지 정의하는 이벤트(Event)와 워크플로우가 트리거되면 실행될 작업(Job)을 포함한다.

<br>

### **이벤트(Event)**

워크플로우에 특정한 이벤트를 정의하면, 해당 이벤트가 저장소에서 트리거되었을 때 워크플로우가 실행된다. PR 생성, 이슈 생성, 커밋 푸시 등이 이벤트에 속한다.

<br>

### **작업(Job)**

워크플로우를 구성하는 실행 단위를 의미한다. 워크플로우내의 모든 작업은 기본적으로는 병렬로 실행된다. 또한, 같은 워크플로우내의 작업들은 서로 종속성이 기본적으로 존재하지 않는다. 작업은 여러개의 단계(Step)을 포함한다.

<br>

### **단계(Step)**

단계는 쉘 스크립트일수도 있고, 일반적인 커맨드일 수도 있다. 작업 내의 단계들은 순차적으로 실행되며, 각 단계는 동일한 러너(Runner)에서 실행되므로 상호 데이터를 공유할 수 있다.

<br>

### **액션(Action)**

복잡하지만 자주 사용되는 작업 단위를 재사용이 가능하도록 만든 실행 단위이다. 액션은 GitHub Market place에서 공유될 수 있다. 그리고 다른 사용자들이 자신의 워크플로우에 다른 사람들이 만든 액션을 가져와 사용할 수 있다.

대표적인 액션으로는 ``actions/checkout`` 이 있는데, 이 액션은 러너에 저장소 코드를 다운로드하고 특정 브랜치로 Checkout 하는 작업을 해준다. 거의 대부분의 CI/CD 작업에는 프로젝트의 소스코드가 필요하므로 정말 많이 사용되는 액션이다.

<br>

### **러너(Runner)**

러너는 GitHub Actions 워크플로우를 실제로 실행하는 서버를 의미한다. GitHub에서는 Ubuntu, Windows, macOS 환경의 러너를 제공한다. 그 외 OS나 특정 하드웨어 스펙에서 실행하고 싶거나, 기타 이유로 GitHub과 독립적인 환경에서 실행하고 싶을 때는 Self-Hosted Runner를 사용할 수 있다.

<br>

## **Workflow 작성하기**

![image](https://stalker5217.netlify.app/static/beaa4f54faa4d888edd95405ba35caf5/5c744/workflow_start.png)

repository의 github action 탭에 들어가면 다음과 같이 repository에 있는 language를 감지하는 화면이 나타난다. 적용할 프로젝트가 spring boot & gradle 기반이므로 표기된 workflow를 선택한다.

```yml
# This workflow will build a Java project with Gradle
# For more information see: https://help.github.com/actions/language-and-framework-guides/building-and-testing-java-with-gradle

# Repo Action 페이지에 나타날 이름 
name: Spring Boot & Gradle CI/CD 

# Event Trigger
# master branch에 push 또는 pull request가 발생할 경우 동작
# branch 단위 외에도, tag나 cron 식 등을 사용할 수 있음 
on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

# CI workflow에서 실행되는 모든 job들을 그룹화한다.
jobs:
  # build라는 이름의 job을 생성한다. 그 하위에는 2개의 step이 존재하는 구조이다.
  build:
    # 실행 환경 지정
    runs-on: ubuntu-latest

    # build 작업에서 실행되는 모든 steps를 그룹화한다. 이 섹션 하위에 중첩된 각 항목은 별도의 작업이거나 셸 스크립트이다.
    steps:
      # uses 키워드는 이 단계에서 action/checkout@/v2 실행하도록 지정한다. 이것은 내 repository를 runner에서 체크아웃하여 스크립트 또는 빌드 및 테스트 도구를 실행할 수 있도록 하는 작업이다. repository의 코드에 대해 workflow가 실행될 때마다 checkout 작업을 사용해야 한다.
    - uses: actions/checkout@v2
    
    - name: Set up JDK 1.8
      uses: actions/setup-java@v1
      with:
        java-version: 1.8
    
    - name: Grant execute permission for gradlew
      run: chmod +x gradlew
    
    - name: Build with Gradle
      run: ./gradlew clean build
```