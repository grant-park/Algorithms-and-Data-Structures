def leftRotate(T,x):
	y = x.right
	x.right = y.left
	if y.left != T.nil:
		y.left.p = x
	y.p = x.p
	if x.p == T.nil:
		T.root = y