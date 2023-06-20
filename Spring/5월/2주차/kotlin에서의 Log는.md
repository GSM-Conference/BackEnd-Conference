# Kotlin에서의 Log는 ??

> Java/Spring 에서는 `Lombok`의 Slf4j를 사용해서 쉽게 로그를 찍을 수 있었다. 그러나 코틀린은 Lombok을 제대로 사용할 수 없기 때문에 Slf4j를 사용할 수 없다. 그럼 이제 kotlin에서 Logger 객체를 생성해 Log를 찍는 법을 알아보자.

## 기본적인 사용법

```kotlin
class Log {
    val log = LoggerFactory.getLogger(Log)

    fun createLog() {
        log.info("로그 찍기")
    }
}
```

## 추상 클래스를 상속받는 companion object

```kotlin
import org.slf4j.LoggerFactory
 
abstract class LoggerCreator {
    val log = LoggerFactory.getLogger(this.javaClass)!!
}
```

```kotlin
@Component
class Log {
    companion object : LoggerCreator()
    
    fun createLog() {
        log.info("로그 찍기")
    }
}
```

## Kotlin Loggin 라이브러리 사용

### Gradle

```kotlin
implementation 'io.github.microutils:kotlin-logging:3.0.5'
```

### Maven
```kotlin
<dependency>
    <groupId>io.github.microutils</groupId>
    <artifactId>kotlin-logging</artifactId>
    <version>3.0.5</version>
</dependency>
```

```kotlin
@Component
class LogTest {
    val log = KotlinLogging.logger {}
 
    fun createLog() {
        log.info("로그 찍기")
    }
}
```

> 결론 : 웬만하면 기본적인 팩토리 메서드를 사용해서 로그를 찍자.