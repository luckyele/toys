function [v] = sigmoid(z)
  v = (1 + e.^(-z)).^(-1);
endfunction