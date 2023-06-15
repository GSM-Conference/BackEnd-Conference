# Filter 

filter 함수는 주어진 람다 조건을 만족하는 원소만 필터링 하는 기능이다.<br>
List와 Set을 필터링 하는 경우에는 filter함수를 사용하고 Map을 필터링하는 경우에는 Map함수를 사용한다.

``` kotlin
val numbers = listOf("one", "two", "three", "four")  
val longerThan3 = numbers.filter { it.length > 3 }
println(longerThan3)
// 결과 : [three, four]

val numbersMap = mapOf("key1" to 1, "key2" to 2, "key3" to 3, "key11" to 11)
val filteredMap = numbersMap.filter { (key, value) -> key.endsWith("1") && value > 10}
println(filteredMap)
// 결과 : {key11=11}
```

+  filterIndexed() : 인덱스를 통해 처리하고 싶을 때 사용하면 인덱스의 값에 접근할 수 있다.
+ filterNot() : 지정된 조건과 일치하는 항목을 제외한 리스트 반환	
```kotlin
val numbers = listOf("one", "two", "three", "four")

val filteredIdx = numbers.filterIndexed { index, s -> (index != 0) && (s.length < 5)  }
val filteredNot = numbers.filterNot { it.length <= 3 }

println(filteredIdx)
println(filteredNot)

// 결과 : [two, four]
//       [three, four]
```

+ filterIsInstance<T>() : 주어진 타입을 만족하는 원소 필터링. T 타입과 관련된 함수를 쓸 수 있다.

```kotlin
val numbers = listOf(null, 1, "two", 3.0, "four")
println("All String elements in upper case:")
numbers.filterIsInstance<String>().forEach {
    println(it.uppercase())
}
// 결과 : All String elements in upper case:
//       TWO
//       FOUR
```

+ partition() : 리스트를 특정 조건에 따라 분리. List나 Set에서 사용할 수 있으며 Map에서는 사용 불가.
>> 이 함수는 `it.length > 3`이라는 조건이 있는데 이 조건에 부합하는 원소들은 match로 이동하고 부합하지 않는 남는 원소들은 rest로 이동한다.

```kotlin
val numbers = listOf("one", "two", "three", "four")
val (match, rest) = numbers.partition { it.length > 3 }

println(match)
println(rest)
// 결과 : [three, four]
//       [one, two]

```


filter 함수가 조건을 만족하는 원소를 찾았다면 any, all, none 함수들은 조건에 맞는 원소가 존재하는지를 확인할 수 있다.

+ any() : 조건을 만족하는 원소가 1개 이상 존재하면 true

+ none() : 조건을 만족하는 원소가 없으면 true

+ all() : 모든 원소가 조건을 만족하면 true

```kotlin
val any = ml.any { it % 2 == 0 }
println("리스트의 짝수인 원소가 존재하나요? ${any.toString()}")

val all = ml.all { it > 1 }
println("리스트의 모든 수가 1보다 큰가요? ${all.toString()}")

val none = ml.none { it > 10 }
println("리스트의 10보다 큰 수가 없나요? ${none.toString()}")

// 결과 : 리스트의 짝수인 원소가 존재하나요? true
//       리스트의 모든 수가 1보다 큰가요? false
//       리스트의 10보다 큰 수가 없나요? true
```

<hr>

# Map
map은 원소를 원하는 형태로 변환하는 기능을 하며 이들의 반환값은 list 입니다.<br>
결과는 원본 리스트와 원소 개수는 같지만, 각 원소는 주어진 람다(함수)에 따라 변환된 **새로운 컬렉션**입니다. 


```kotlin
val people = listOf(Person("Alice", 29), Person("Bob", 31))
println(people.map { it.name })
// 결과 : [Alice, Bob]
```

```kotlin
val list = listOf(1, 2, 3, 4)
println(list.map { it * it }) //제곱 만들기 (1x1, 2x2, 3x3, 4x4)
// 결과 : [1, 4, 9, 16]
```
![img](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FXwSjl%2FbtqC9NXpnGf%2FLuehVXHm7ZRNo4l4t0i3d0%2Fimg.jpg)

map 함수는 람다를 컬렉션의 모든 원소에 적용한 결과로 이루어진 새로운 컬렉션입니다.
