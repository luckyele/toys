function [] = display_m(X, level)
    
  S = zeros(1,24);
  
  for (i = 1:106)
    if X(i,24) == level,
      S = [S;X(i,:)];
    endif
  endfor
    
  for (i = 1:24)
    subplot(4, 6, i);
    hist(S(:,i),'b');
  endfor
  
  