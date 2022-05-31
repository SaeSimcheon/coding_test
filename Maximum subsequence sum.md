

$$
MaxSum(i) = Max(Sum(0->i),Sum(1->i),Sum(2->i),...,Sum(i->i))
$$

$$
Sum(x->i+1) = Sum(x->i) + Data(i+1) 
$$

$Data(i+1)$ is the element value at at index i+1.

$$
MaxSum(i+1) = Max(Sum(0->i) + Data(i+1), Sum(1->i) + Data(i+1), ..., Sum(i->i) + Data(i+1), Data(i+1))
$$

$$
Max(a+y,b+y,c+y) = Max(a,b,c) +y
$$

$$
MaxSum(i+1) = Max(Max(Sum(0->i), Sum(1->i), ..., Sum(i->i))+ Data(i+1), Data(i+1))
$$

$$
MaxSum(i+1) = Max(MaxSum(i)+ Data(i+1), Data(i+1))
$$

