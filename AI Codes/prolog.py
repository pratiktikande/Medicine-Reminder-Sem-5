#SIMPLE

likes(sam, salad).
likes(sam, pie).
likes(sam, apples).
likes(sam, whiskey).
likes(sam, anime).

#COUNT
count([],0).
count([H|T],N) :- count(T,N1) , N is N1+1.

#Greatest of 3 number
max(P,Q,R):-P>Q,P>R,write('Larger number is '),write(P).
max(P,Q,R):-P<Q,Q>R,write('Larger number is '),write(Q).
max(P,Q,R):-R>Q,P<R,write('Larger number is '),write(R).
max(P,Q,R):-P=Q,P<R,write('Larger number is '),write(R).
max(P,Q,R):-P<Q,P=R,write('Larger number is '),write(Q).
max(P,Q,R):-Q=R,P>Q,write('Larger number is '),write(P).
max(P,Q,R):-P=Q,P>R,write('Larger numbers are  '),write(P),write(' and '),write(Q).
max(P,Q,R):-P=R,Q<R,write('Larger numbers are  '),write(P),write(' and '),write(R).
max(P,Q,R):-Q=R,P<R,write('Larger numbers are  '),write(R),write(' and '),write(Q).
max(P,Q,R):-P=Q,P=R,write('All numbers are equal '). 

#Factorial
factorial(0, 1).
 factorial(N, F) :- 
       N > 0, 
       Prev is N -1, 
       factorial(Prev, R), 
       F is R * N.
