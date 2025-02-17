vars
	x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 x16 x17 x18 x19 

rules
	x1 >= 1 , x3 >= 1 , x10 >= 2 , x15 >= 2 ->
		x0' = x0+1,
		x1' = x1-1,
		x2' = x2+1,
		x3' = x3-1,
		x5' = x5+1,
		x10' = x10-2,
		x15' = x15-2;

	x0 >= 1 , x2 >= 1 , x3 >= 1 , x5 >= 1 , x8 >= 1 , x15 >= 1 , x16 >= 1 , x17 >= 1 , x19 >= 1 ->
		x0' = x0-1,
		x2' = x2-1,
		x3' = x3-1,
		x12' = x12+3,
		x14' = x14+1,
		x15' = x15-1,
		x17' = x17-1,
		x18' = x18+1,
		x19' = x19-1;

	x1 >= 1 , x2 >= 1 , x17 >= 1 ->
		x1' = x1-1,
		x2' = x2-1,
		x9' = x9+1,
		x11' = x11+1,
		x14' = x14+1,
		x15' = x15+1,
		x17' = x17-1;

	x7 >= 1 , x10 >= 1 , x12 >= 1 , x15 >= 1 ->
		x9' = x9+1,
		x10' = x10-1,
		x11' = x11+1,
		x12' = x12-1,
		x15' = x15-1,
		x16' = x16+1;

	x8 >= 1 , x9 >= 1 , x11 >= 3 , x12 >= 1 , x15 >= 1 ->
		x2' = x2+1,
		x3' = x3+1,
		x6' = x6+2,
		x7' = x7+1,
		x8' = x8-1,
		x11' = x11-3,
		x12' = x12-1,
		x13' = x13+1,
		x15' = x15-1,
		x19' = x19+1;

	x0 >= 1 , x2 >= 1 , x4 >= 2 , x5 >= 1 , x8 >= 1 , x10 >= 1 , x16 >= 1 , x17 >= 1 ->
		x0' = x0+1,
		x2' = x2-1,
		x4' = x4-2,
		x5' = x5-1,
		x8' = x8-1,
		x11' = x11+1,
		x15' = x15+1;

	x0 >= 1 , x2 >= 2 , x6 >= 1 , x7 >= 1 , x11 >= 1 , x13 >= 1 , x14 >= 2 ->
		x0' = x0-1,
		x2' = x2-2,
		x6' = x6-1,
		x7' = x7-1,
		x9' = x9+1,
		x11' = x11-1,
		x13' = x13-1,
		x14' = x14-2;

	x2 >= 1 , x3 >= 1 , x4 >= 1 , x9 >= 1 , x15 >= 1 , x16 >= 1 ->
		x2' = x2-1,
		x4' = x4-1,
		x6' = x6+1,
		x7' = x7+1,
		x9' = x9-1,
		x10' = x10+1,
		x14' = x14+1,
		x16' = x16-1,
		x18' = x18+1;

	x6 >= 2 , x7 >= 1 , x11 >= 1 , x18 >= 1 , x19 >= 1 ->
		x4' = x4+1,
		x5' = x5+1,
		x6' = x6-2,
		x9' = x9+1,
		x10' = x10+1,
		x11' = x11-1,
		x14' = x14+1,
		x15' = x15+2,
		x18' = x18-1,
		x19' = x19-1;

	x8 >= 2 , x9 >= 1 , x16 >= 1 ->
		x8' = x8-2,
		x16' = x16-1,
		x18' = x18+1;

	x0 >= 1 , x1 >= 1 , x5 >= 2 , x10 >= 1 , x13 >= 1 , x15 >= 1 , x16 >= 1 ->
		x0' = x0-1,
		x1' = x1-1,
		x2' = x2+1,
		x3' = x3+1,
		x7' = x7+1,
		x10' = x10-1,
		x13' = x13-1,
		x14' = x14+1,
		x16' = x16-1,
		x19' = x19+1;

	x14 >= 1 ->
		x0' = x0+1,
		x9' = x9+1,
		x10' = x10+1,
		x13' = x13+1,
		x14' = x14-1;

	x5 >= 1 , x9 >= 1 , x14 >= 1 , x17 >= 1 , x19 >= 1 ->
		x1' = x1+1,
		x5' = x5-1,
		x7' = x7+1,
		x8' = x8+1,
		x9' = x9-1,
		x10' = x10+3,
		x14' = x14-1,
		x17' = x17-1,
		x19' = x19-1;

	x5 >= 1 , x7 >= 1 , x12 >= 2 , x14 >= 2 ->
		x12' = x12-2,
		x14' = x14-2,
		x17' = x17+1,
		x18' = x18+1;

	x13 >= 1 ->
		x14' = x14+1;

	x14 >= 1 , x16 >= 1 ->
		x1' = x1+2,
		x2' = x2+2,
		x14' = x14-1,
		x16' = x16+1,
		x18' = x18+1,
		x19' = x19+2;

	x2 >= 1 , x3 >= 1 , x8 >= 1 , x13 >= 1 , x18 >= 1 ->
		x2' = x2-1,
		x3' = x3-1,
		x7' = x7+1,
		x8' = x8-1,
		x9' = x9+2,
		x13' = x13-1,
		x18' = x18-1;

	x4 >= 3 ->
		x4' = x4-3,
		x13' = x13+1;

	x0 >= 1 , x1 >= 1 , x2 >= 2 , x5 >= 1 , x11 >= 1 , x12 >= 1 ->
		x2' = x2-2,
		x3' = x3+1,
		x5' = x5-1,
		x6' = x6+1,
		x12' = x12-1,
		x13' = x13+2,
		x19' = x19+1;

	x5 >= 1 , x10 >= 1 , x19 >= 1 ->
		x1' = x1+1,
		x5' = x5-1,
		x14' = x14+1,
		x15' = x15+1,
		x17' = x17+2,
		x19' = x19-1;

	x1 >= 1 , x2 >= 1 , x4 >= 2 , x9 >= 1 , x13 >= 1 ->
		x1' = x1-1,
		x2' = x2-1,
		x3' = x3+1,
		x4' = x4-2,
		x5' = x5+1,
		x6' = x6+1,
		x9' = x9-1,
		x12' = x12+1,
		x13' = x13-1,
		x14' = x14+2,
		x16' = x16+1,
		x19' = x19+1;

	x14 >= 1 , x18 >= 1 ->
		x1' = x1+1,
		x5' = x5+1,
		x6' = x6+2,
		x11' = x11+1,
		x16' = x16+1,
		x17' = x17+1,
		x18' = x18-1;

	x4 >= 1 ->
		x1' = x1+1,
		x2' = x2+1,
		x4' = x4-1,
		x8' = x8+1,
		x10' = x10+1,
		x14' = x14+2,
		x15' = x15+2,
		x18' = x18+1;

	x6 >= 1 , x13 >= 1 ->
		x4' = x4+1,
		x5' = x5+1,
		x6' = x6-1,
		x13' = x13-1,
		x18' = x18+1;

	x9 >= 1 , x12 >= 1 , x14 >= 1 , x15 >= 1 , x19 >= 1 ->
		x0' = x0+1,
		x6' = x6+1,
		x7' = x7+1,
		x9' = x9-1,
		x12' = x12-1,
		x14' = x14-1,
		x15' = x15-1,
		x16' = x16+1,
		x19' = x19-1;

	x2 >= 3 , x12 >= 1 , x13 >= 1 , x16 >= 2 , x19 >= 1 ->
		x2' = x2-3,
		x8' = x8+1,
		x12' = x12-1,
		x13' = x13-1,
		x15' = x15+1,
		x16' = x16-2,
		x19' = x19-1;

	x8 >= 2 ->
		x1' = x1+1,
		x4' = x4+1,
		x5' = x5+1,
		x8' = x8-2,
		x10' = x10+1,
		x12' = x12+1,
		x16' = x16+1,
		x18' = x18+1;

	x12 >= 1 , x17 >= 2 ->
		x7' = x7+1,
		x8' = x8+4,
		x12' = x12-1,
		x15' = x15+1,
		x17' = x17-2,
		x18' = x18+1,
		x19' = x19+1;

	x4 >= 1 , x12 >= 1 ->
		x1' = x1+1,
		x12' = x12-1,
		x17' = x17+1;

	x5 >= 1 , x7 >= 1 , x16 >= 1 , x19 >= 1 ->
		x0' = x0+1,
		x3' = x3+1,
		x5' = x5-1,
		x7' = x7-1,
		x12' = x12+1,
		x16' = x16-1,
		x19' = x19-1;

	x1 >= 1 , x2 >= 1 , x6 >= 1 , x7 >= 1 , x10 >= 1 , x13 >= 2 , x17 >= 1 ->
		x1' = x1+1,
		x4' = x4+1,
		x7' = x7-1,
		x8' = x8+1,
		x10' = x10-1,
		x13' = x13-2,
		x16' = x16+1,
		x17' = x17-1,
		x18' = x18+1;

	x6 >= 1 ->
		x1' = x1+1,
		x3' = x3+1,
		x6' = x6-1,
		x7' = x7+1,
		x13' = x13+1,
		x14' = x14+1,
		x17' = x17+1,
		x19' = x19+1;

	x13 >= 1 , x16 >= 1 ->
		x11' = x11+1,
		x13' = x13-1,
		x16' = x16-1;

	x5 >= 2 ->
		x3' = x3+1,
		x5' = x5-2,
		x9' = x9+1;

	x10 >= 2 , x12 >= 1 , x15 >= 2 , x16 >= 1 , x18 >= 2 ->
		x4' = x4+1,
		x6' = x6+1,
		x10' = x10-1,
		x14' = x14+2,
		x15' = x15-2,
		x16' = x16-1,
		x17' = x17+1,
		x18' = x18-2;

	x6 >= 1 , x7 >= 1 , x11 >= 3 , x12 >= 1 , x14 >= 1 , x19 >= 1 ->
		x6' = x6-1,
		x7' = x7-1,
		x11' = x11-3,
		x12' = x12-1,
		x14' = x14-1,
		x16' = x16+1,
		x19' = x19-1;

	x3 >= 2 , x5 >= 1 , x15 >= 1 ->
		x2' = x2+1,
		x3' = x3-2,
		x5' = x5-1,
		x9' = x9+1,
		x11' = x11+1,
		x15' = x15-1,
		x19' = x19+1;

	x1 >= 1 ->
		x0' = x0+1,
		x1' = x1-1,
		x5' = x5+2,
		x7' = x7+2,
		x13' = x13+1,
		x19' = x19+1;

	x3 >= 1 ->
		x2' = x2+1,
		x3' = x3-1,
		x4' = x4+1,
		x10' = x10+1,
		x12' = x12+1,
		x15' = x15+1;

	x1 >= 1 , x14 >= 2 , x15 >= 1 , x16 >= 1 , x17 >= 1 ->
		x1' = x1-1,
		x12' = x12+1,
		x14' = x14-2,
		x15' = x15-1,
		x16' = x16-1,
		x17' = x17-1;

	x6 >= 1 , x18 >= 1 ->
		x0' = x0+1,
		x8' = x8+1,
		x10' = x10+1,
		x11' = x11+1,
		x14' = x14+1,
		x18' = x18-1;

	x12 >= 1 , x15 >= 3 , x16 >= 1 ->
		x2' = x2+1,
		x6' = x6+1,
		x10' = x10+1,
		x12' = x12-1,
		x13' = x13+1,
		x15' = x15-2,
		x17' = x17+1;

	x5 >= 1 , x7 >= 1 ->
		x1' = x1+1,
		x2' = x2+1,
		x6' = x6+1,
		x7' = x7-1,
		x11' = x11+1,
		x12' = x12+1,
		x16' = x16+1;

	x0 >= 3 , x4 >= 1 , x6 >= 1 , x8 >= 1 , x9 >= 2 , x16 >= 1 , x18 >= 1 ->
		x0' = x0-3,
		x1' = x1+3,
		x3' = x3+2,
		x4' = x4-1,
		x6' = x6-1,
		x9' = x9-1,
		x11' = x11+1,
		x16' = x16-1;

	x2 >= 1 , x9 >= 1 , x10 >= 1 , x15 >= 1 , x19 >= 1 ->
		x3' = x3+1,
		x7' = x7+1,
		x9' = x9-1,
		x10' = x10-1,
		x11' = x11+1,
		x13' = x13+2,
		x18' = x18+1,
		x19' = x19-1;

	x0 >= 1 , x6 >= 1 , x7 >= 1 , x10 >= 1 , x18 >= 1 , x19 >= 1 ->
		x0' = x0-1,
		x1' = x1+1,
		x4' = x4+1,
		x6' = x6-1,
		x7' = x7-1,
		x8' = x8+1,
		x9' = x9+1,
		x10' = x10-1,
		x11' = x11+1,
		x13' = x13+2,
		x14' = x14+1,
		x17' = x17+1,
		x18' = x18-1,
		x19' = x19-1;

	x0 >= 2 , x2 >= 1 , x4 >= 1 , x9 >= 1 , x16 >= 1 , x19 >= 1 ->
		x0' = x0-2,
		x2' = x2+2,
		x3' = x3+1,
		x4' = x4-1,
		x6' = x6+1,
		x9' = x9-1,
		x13' = x13+2,
		x16' = x16-1,
		x19' = x19-1;

	x5 >= 1 , x12 >= 1 , x14 >= 2 ->
		x3' = x3+1,
		x5' = x5-1,
		x11' = x11+1,
		x12' = x12-1,
		x14' = x14-2,
		x16' = x16+1;

	x0 >= 1 , x3 >= 1 , x15 >= 2 , x19 >= 1 ->
		x0' = x0-1,
		x1' = x1+1,
		x3' = x3-1,
		x4' = x4+1,
		x10' = x10+1,
		x11' = x11+1,
		x12' = x12+1,
		x15' = x15-1,
		x16' = x16+2,
		x18' = x18+1,
		x19' = x19-1;

	x5 >= 1 , x10 >= 1 ->
		x10' = x10-1,
		x17' = x17+1;

	x1 >= 1 ->
		x0' = x0+1,
		x1' = x1-1,
		x3' = x3+1,
		x5' = x5+1,
		x15' = x15+2;

	x0 >= 1 , x3 >= 1 , x6 >= 1 , x9 >= 1 , x14 >= 1 , x15 >= 1 , x16 >= 1 , x18 >= 1 , x19 >= 1 ->
		x0' = x0-1,
		x1' = x1+1,
		x3' = x3-1,
		x5' = x5+1,
		x6' = x6-1,
		x8' = x8+3,
		x9' = x9-1,
		x13' = x13+1,
		x14' = x14-1,
		x15' = x15-1,
		x16' = x16+1,
		x18' = x18-1;

	x0 >= 1 , x7 >= 1 , x8 >= 1 , x10 >= 1 , x11 >= 1 ->
		x1' = x1+1,
		x5' = x5+2,
		x7' = x7-1,
		x8' = x8-1,
		x10' = x10-1,
		x11' = x11-1;

	x0 >= 2 , x10 >= 1 , x11 >= 1 , x16 >= 1 ->
		x0' = x0-2,
		x10' = x10-1,
		x11' = x11-1,
		x12' = x12+1;

	x1 >= 1 , x3 >= 2 , x4 >= 2 , x5 >= 2 , x13 >= 1 ->
		x0' = x0+1,
		x1' = x1-1,
		x3' = x3-2,
		x4' = x4-1,
		x5' = x5-2,
		x8' = x8+1,
		x16' = x16+1,
		x17' = x17+1,
		x19' = x19+1;

	x3 >= 2 , x6 >= 2 , x11 >= 2 , x16 >= 1 , x18 >= 1 ->
		x3' = x3-2,
		x6' = x6-2,
		x11' = x11-2,
		x13' = x13+1,
		x15' = x15+1,
		x16' = x16-1,
		x18' = x18-1,
		x19' = x19+1;

	x0 >= 1 , x3 >= 1 , x4 >= 1 , x9 >= 1 , x12 >= 1 , x14 >= 1 ->
		x0' = x0-1,
		x1' = x1+1,
		x2' = x2+1,
		x3' = x3-1,
		x7' = x7+1,
		x8' = x8+1,
		x9' = x9-1,
		x11' = x11+1,
		x12' = x12-1,
		x13' = x13+1,
		x17' = x17+1;

	x0 >= 1 ->
		x4' = x4+2,
		x15' = x15+1,
		x17' = x17+1;

	x2 >= 1 , x14 >= 1 , x19 >= 1 ->
		x0' = x0+1,
		x14' = x14-1,
		x19' = x19-1;

	x0 >= 1 , x1 >= 1 , x3 >= 1 , x5 >= 1 , x9 >= 2 , x12 >= 2 , x13 >= 1 ->
		x0' = x0-1,
		x1' = x1-1,
		x2' = x2+1,
		x3' = x3-1,
		x9' = x9-2,
		x12' = x12-2,
		x13' = x13-1,
		x19' = x19+1;

	x7 >= 2 ->
		x4' = x4+1,
		x6' = x6+1,
		x7' = x7-2,
		x12' = x12+1,
		x13' = x13+1;

	x5 >= 1 , x6 >= 1 , x15 >= 1 , x16 >= 1 ->
		x5' = x5-1,
		x6' = x6-1,
		x13' = x13+1,
		x14' = x14+1,
		x15' = x15-1,
		x16' = x16-1;

	x2 >= 1 , x3 >= 1 , x5 >= 1 , x10 >= 1 , x16 >= 1 , x18 >= 1 ->
		x2' = x2-1,
		x3' = x3-1,
		x7' = x7+1,
		x10' = x10-1,
		x16' = x16-1,
		x18' = x18-1;

	x0 >= 1 , x1 >= 1 , x5 >= 1 , x6 >= 1 , x9 >= 2 , x12 >= 1 , x18 >= 1 ->
		x0' = x0-1,
		x1' = x1-1,
		x5' = x5-1,
		x6' = x6-1,
		x9' = x9-2,
		x11' = x11+1,
		x12' = x12-1,
		x14' = x14+1,
		x18' = x18-1;

	x0 >= 1 , x2 >= 1 , x3 >= 1 , x5 >= 2 , x11 >= 1 , x13 >= 1 , x15 >= 2 ->
		x0' = x0-1,
		x2' = x2-1,
		x3' = x3-1,
		x5' = x5-2,
		x6' = x6+1,
		x8' = x8+1,
		x10' = x10+1,
		x11' = x11-1,
		x14' = x14+1,
		x15' = x15-2,
		x17' = x17+1;

	x3 >= 1 , x8 >= 1 , x17 >= 1 , x18 >= 1 ->
		x2' = x2+1,
		x3' = x3-1,
		x8' = x8-1,
		x9' = x9+2,
		x14' = x14+1,
		x17' = x17-1,
		x19' = x19+2;

	x1 >= 2 , x2 >= 1 , x9 >= 1 , x19 >= 1 ->
		x1' = x1-2,
		x2' = x2-1,
		x9' = x9-1,
		x14' = x14+1,
		x15' = x15+1,
		x19' = x19-1;

	x14 >= 1 , x18 >= 1 ->
		x2' = x2+1,
		x6' = x6+1,
		x7' = x7+1,
		x9' = x9+1,
		x13' = x13+1,
		x18' = x18-1,
		x19' = x19+1;

	x2 >= 1 , x4 >= 1 , x11 >= 1 , x16 >= 1 , x19 >= 1 ->
		x2' = x2-1,
		x11' = x11-1,
		x14' = x14+1,
		x16' = x16-1,
		x17' = x17+1,
		x19' = x19-1;

	x1 >= 1 ->
		x1' = x1-1,
		x7' = x7+2,
		x9' = x9+1,
		x14' = x14+1,
		x17' = x17+1;

init
	x0 = 0 , x1 = 0 , x2 = 1 , x3 = 1 , x4 = 2 , x5 = 0 , x6 = 1 , x7 = 0 , x8 = 0 , x9 = 0 , x10 = 0 , x11 = 0 , x12 = 1 , x13 = 0 , x14 = 0 , x15 = 0 , x16 = 0 , x17 = 1 , x18 = 1 , x19 = 0