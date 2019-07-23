function [] = draw_all(x)

  for (i = 1:16)
    subplot(4,4,i);
    hist(draw_scatter(x, i));

  endfor
  
endfunction