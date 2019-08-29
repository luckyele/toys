function D = dv(data)
  D = zeros(207,16);
  i = 1;
  while i <=16,
    D(:,i) = st(data,i); 
    i = i + 1;
  end;
  