function [theta, J_history] = gredientDescent(X,y,alpha,iteration);
  
  [m,n]=size(X);
  theta = zeros(n,1);
  for(i= 1:iteration)
     [J,grad] = costFunction(theta,X,y);
     J_history(i) = J;
     theta = theta-X'*(sigmoid(X*theta)-y)*alpha/m;
     if  mod(i,100)==0,
      disp(sprintf('after %d iter the J=%f theta= ',i,J));
      disp(theta');
     endif
  endfor
   
endfunction