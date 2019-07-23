function a = draw_scatter(X, index)
  n = size(X)(1); 
  m = size(X)(2);
  a = [0];
  
  for (i = 1 : n)   
    if X(:,m)(i) == 3,
      a = [a (X(i,:)(index))];
    endif
  endfor
endfunction;