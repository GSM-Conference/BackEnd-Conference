### Gradle은 Groovy를 기반으로 한 빌드 도구 이다.

아래는 Gradle이 자동화 시켜주는 Tack(Gradle의 실행 작업 단위)들이다.

- **Complie**
- **Test**
- **Packaging**
- **Deploy & Run**

<aside>
Complie : Kotlin 파일이나 Java 파일을 바이트 코드로 변환시켜주는 작업 <br>
Test : 애플리케이션에 대한 Test 코드를 실행시켜준다.<br>
Packaging : 애플리케이션을 패키징 해 jar, war 파일로 만들어준다.<br>
Deploy & Run : 애플리케이션을 돌려 서버를 실행 시켜주는 것 이다.<br>

</aside>

---

### Gradle은 다음과 같은 특징이 있다.

- Gradle을 설치 없이 Gradle Wrapper를 이용하여 빌드를 할 수 있다.
- JVM에서 실행되기 때문에 JDK 설치가 필요하다.
- 빌드 속도가 Maven보다 10~100배 빠르다.
- Ant → Maven → Gradle 순으로 사용되었다.
- Ant, Maven을 Gradle로 간단하게 변환 할 수 있다.

### 기본 구조

```java
project/
		gradlew
		gradlew.bat
		gradle/warpper/
				gradle-wrapper.jar
				gradle-wrapper.properties
		build.gradle
		settings.gradle
```

- **gradlew**: 리눅스 또는 맥OS용 실행 스크립트 파일이다.
- **gradlew.bat**: 윈도우용 실행 배치 스크립트이다.
- **gradle-wrapper.jar**: wrapper 파일
로컬 환경에 gradle을 설치 하지 않고도 gradlew, gradlew.bat이 
이 파일을 사용하여 gradle task를 실행한다.
- **gradle-wrapper.properties**: wrapper의 설정파일
이 설정 파일의 wrapper 버전 등을 변경하면, gradle task 실행시 자동으로 새로운 wrapper 파일을 로컬 캐시에 다운로드 받는다.
- **build.gradle:** 
프로젝트의 라이브러리 의존성, 플러그인, 라이브러리 저장소 등을 설정할 수 있는 빌드 스크립트 파일이다.
- **settings.gradle:** 프로젝트의 구성 정보 파일이다.

---

### repositories 메서드

프로젝트에서 사용하는 라이브러리의 위치를 지정한다.

```java
repositories {
    mavenCentral()
}
```

<img width="499" alt="image" src="https://github.com/GSM-Conference/BackEnd-Conference/assets/82089918/ec68d4bc-1f51-45f2-b98b-b4d12893cd75">

### ext 메서드

build.gradle에서 전역변수로 변수를 사용하기 위해서 사용된다.

```java
ext {
		quertDslVersion = '4.4.0'
}
```

---

### Complie(api) vs **implementation**

<img width="723" alt="image" src="https://github.com/GSM-Conference/BackEnd-Conference/assets/82089918/2c500789-04cf-4df8-8190-ea2ec8eec7df">


- **Complie(api)**를 사용하는 경우
Complie은 implementation 보다 더 많은 라이브러리를 빌드하기 때문에
A라는 모듈을 수정하면, 이 모듈을 의존하고 있는 B와 C는 모두 재 빌드 된다.

- **implementation**를 사용하는 경우
    
    B라는 모듈을 수정하면, 직접 의존하는 B만 재빌드 한다.
    

---

### Gradle의 속도가 빠른 이유

- **점진적 빌드:**
이미 빌드 된 파일들은 빌드 대상에서 제외 시키고 빌드 한다.
ex) 20개의 파일중 15개는 이미 빌드된 파일이면 5개만 빌드한다.
- **Build Cache**:
    
    빌드 한 결과물을 캐시로 저장하여 이전 빌드의 결과물을 다른 빌드에 사용할 수 있다.
    
- **Daemon Process**:
    
    빌드 결과물을 메모리 상에 저장하여, 한번 빌드 된 프로젝트들은 다음 빌드에서 매우 적은 시간만 소요 된다.