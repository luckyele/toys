function [J, grad] = costFunction(theta, X, y)
m = length(y);
J = 0;
grad = zeros(size(theta));
 
tmp = ones(m,1);
h  = sigmoid(X*theta);
h1 = log(h);
h2 = log(tmp-h);
 
y2 = tmp-y;
 
J = (y'*h1+y2'*h2)/(-m);
 
grad = (X'*(h-y))/m;
end