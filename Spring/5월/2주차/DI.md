# **의존관계 주입(Dependency Injection)**

## **의존관계(Dependency)란?**
의존관계 주입(Dependency Injection)에 대하여 알아보기 전에 의존관계가 무엇인지 알아야 한다. 

의존관계는 의존 대상 B가 변하면, 그것이 A에 영향을 미칠 때 A는 B와 의존관계라 한다.   
쉽게 말해 B가 변경되었을 때 그 영향이 A에 미치는 관계를 말한다.

예를 들어 다음과 같은 상황을 가정해보자.

> 피자 가게 요리사는 피자 레시피에 의존한다. 만약 피자 레시피가 변경된다면, 요리사는 피자를 새로운 방법으로 만들게 된다. 레시피의 변화가 요리사에게 영향을 미쳤기 때문에 **요리사는 레시피에 의존한다**라고 할 수 있다.

이를 코드로 나타내면 다음과 같다.

```java
public class PizzaChef{
	
	private PizzaRecipe pizzaRecipe;
	
	public PizzaChef() {
		this.pizzaRecipe = new PizzaRecipe();
	}
	
}
```
PizzaChef 객체는 PizzaRecipe 객체의 의존 관계가 있다. 이러한 구조는 다음과 같은 큰 문제점들을 가진다.

<br>

### **1. 두 클래스의 결합성이 높다**
PizzaChef 클래스는 PizzaRecipe 클래스와 **강하게 결합되어 있다는 문제점**을 가지고 있다. 만약 PizzaChef가 새로운 레시피인 CheezePizzaRecipe 클래스를 이용해야 한다면 PizzaChef 클래스의 생성자를 변경해야만 한다. 만약 이후 레시피가 계속해서 바뀐다면 매번 생성자를 바꿔줘야 하는 등, 유연성이 떨어지게 된다.

<br>

### **2. 객체들 간의 관계가 아닌 클래스 간의 관계가 맺어진다**
객체 지향 5원칙(SOLID)중 "추상화(인터페이스)에 의존해야지, 구체화(구현 클래스)에 의존하면 안 된다"라는 DIP원칙이 존재한다. 현재 PizzaChef 클래스는 PizzaRecipe 클래스와 의존 관계가 있다. 즉, PizzaChef는 클래스에 의존하고 있다. 이는 객체 지향 5원칙을 위반하는 것으로 PizzaChef 클래스의 변경이 어려워지게 된다.

이러한 문제점들을 해결할 수 있는 것이 바로 의존관계 주입(DI)이다.

<br>

## **의존 관계 주입(DI)이란?**
**DI는 의존 관계를 외부에서 결정(주입)해주는 것을** 말한다. 스프링에서는 이러한 DI를 담당하는 DI 컨테이너가 존재한다. 이 DI 컨테이너가 객체들 간의 의존 관계를 주입한다.

위의 문제점을 DI를 이용해 해결해보면 우선 다양한 피자 레시피를 추상화하기 위해 PizzaRecipe를 interface로 만들고 이후 다양한 종류의 피자 레시피는 이 PizzaRecipe 인터페이스를 구현하는 식으로 작성하면 된다.

```java
public interface PizzaRecipe{
	
}

public class CheesePizzaRecipe implements PizzaRecipe{
	
}
```

이제 PizzaChef 클래스의 생성자에서 외부로부터 피자 레시피를 주입(injection) 받도록 변경한다.

```java
public class PizzaChef{
	
	private PizzaRecipe pizzaRecipe;
	
	public PizzaChef(PizzaRecipe pizzaRecipe) {
		this.pizzaRecipe = pizzaRecipe;
	}
	
}
```

이때 스프링의 DI 컨테이너가 애플리케이션 실행 시점에 필요한 객체를 생성하여 PizzaChef 클래스에 주입해주는 역할을 한다. 예를 들어 다음과 같이 동작한다.

```java
// DI 컨테이너에서의 동작

PizzaChef = new PizzaChef(new CheesePizzaRecipe());

// 만약 치즈 피자 레시피에서 베이컨 피자 레시피로 바뀐다면?

PizzaChef = new PizzaChef(new BaconPizzaRecipe());
```

<br>

## **의존 관계 주입 방법**
스프링 공식 문서에 따르면 DI는 다음과 같은 2가지 주요 방법을 가진다고 한다.

1.생성자 주입 방법 (Constructor-based Dependency Injection)   
2.수정자 주입 방법 (Setter-based Dependency Injection)

생성자 주입 방법은 위에서 본 것처럼 생성자를 이용해 의존 관계를 주입한 것이다. 생성자 주입은 생성자의 호출 시점에 1회 호출되는 것이 보장된다. 따라서 주입받은 객체가 변하지 않거나, 반드시 객체의 주입이 필요한 경우에 사용 할 수 있다.

수정자 주입 방법은 객체의 Setter를 이용해 의존 관계를 주입하는 것이다.
예를 들어 아래와 같다.

```java
public class PizzaChef{
	
	private PizzaRecipe pizzaRecipe;
	
	public setPizzaRecipe(PizzaRecipe pizzaRecipe) {
		this.pizzaRecipe = pizzaRecipe;
	}
	
}

PizzaChef pizzaChef = new PizzaChef();

pizzaChef.setPizzaRecipe(new CheesePizzaRecipe());
```

이러한 수정자 주입 방법은 생성자 주입과는 다르게 주입받는 객체가 변경될 가능성이 있는 경우에 사용한다.

이외에도 필드 주입, 일반 메서드 주입 등의 방법이 있지만, 스프링은 생성자 주입을 사용하기를 권장한다. 의존 관계 주입의 변경이 필요한 상황은 거의 없다. 하지만 수정자 주입이나 일반 메서드 주입을 이용하면 불필요하게 수정의 가능성을 열어두게 된다. 생성자 주입을 통해 변경의 가능성을 배제하고, 불변성을 보장하는 것이 좋다.

<br>

## **의존 관계 주입의 장점**

### **1. 결합도가 줄어든다**
어떤 객체가 다른 객체에 의존한다는 것은, 그 의존 대상의 변화에 취약하다는 뜻이다. DI를 이용하면 주입받는 대상이 바뀔지 몰라도 해당 객체의 구현 자체를 수정할 일은 없어진다.

<br>

### **2. 유연성이 높아진다**
기존 PizzaChef 클래스는 피자 레시피를 바꾸는 것이 쉽지 않았다. 생성자 코드 자체를 변경해주어야 했지만, DI를 이용하면 생성자의 인수만 다른 피자 레시피로 바꿔주면 된다.

<br>

### **3. 테스트하기 쉬워진다**
DI를 이용한 객체는 자신이 의존하고 있는 인터페이스가 어떤 클래스로 구현되어 있는지 몰라도 된다. 따라서 테스트하기 더 쉬워진다.

<br>

### **4. 가독성이 높아진다**


