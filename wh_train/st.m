function Y = st(X, i)
	max_v = max(X(:,i));
	min_v = min(X(:,i));
	Y = (X(:,i) .- min_v) ./ (max_v - min_v);
