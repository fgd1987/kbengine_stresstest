# -*- coding: utf-8 -*-
import math
import Math

datas={
	1: [
	],
	1001: [
		(40001005, (-112.9299, 1.5, -155.922),(0.0,0.0,0.0), 1),
		(1001, (-102.9299, 1.5, -150.922),(0.0,0.0,0.0), 1),
		(1002, (-105.0, 1.5, -150.922),(0.0,0.0,0.0), 1),
		(1003, (-132.9299, 1.5, -150.922),(0.0,0.0,0.0), 1),
		(1003, (-137.833725, 1.5, -202.246201),(0.0,0.0,0.0), 1),
		(1003, (-146.968063, 1.5, -231.600098),(0.0,0.0,0.0), 1),
		(1003, (-94.462944, 1.5, -195.883881),(0.0,0.0,0.0), 1),
		(1003, (-103.794640, 1.5, -220.648834),(0.0,0.0,0.0), 1),
		(1003, (-83.443954, 1.5, -239.645569),(0.0,0.0,0.0), 1),
		(1003, (-72.320412, 1.5, -219.838470),(0.0,0.0,0.0), 1),
		(1004, (-69.049957, 1.5, -175.957031),(0.0,0.0,0.0), 1),
		(1004, (-60.296272, 1.5, -220.473770),(0.0,0.0,0.0), 1),
		(1004, (-44.794971, 1.5, -200.343048),(0.0,0.0,0.0), 1),
		(1004, (-41.807720, 1.5, -160.731979),(0.0,0.0,0.0), 1),
		(1004, (-61.230453, 1.5, -144.657440),(0.0,0.0,0.0), 1),
		(1004, (-71.636917, 1.5, -140.565033),(0.0,0.0,0.0), 1),
		(1004, (-73.323441, 1.5, -160.713318),(0.0,0.0,0.0), 1),
		(1004, (-53.436718, 1.5, -125.980476),(0.0,0.0,0.0), 1),
		(1004, (-64.340378, 1.5, -121.070831),(0.0,0.0,0.0), 1),
		(40001001, (-34.340378, 1.5, -121.070831),(0.0,0.0,0.0), 1),
		(40001003, (-20.340378, 1.5, -150.070831),(0.0,0.0,0.0), 1),
	],
	3001: [
		(40001002, (10, 1.5, 0),(0.0,0.0,0.0), 1),
	],
}

import copy
import GlobalConst

idx = 1001
cellspace = datas[idx]

r = 360.0 / GlobalConst.MAX_STRESSTEST_CELL_SPACE 
b = 0
a = 60				# 移动半径距离在30米内

for i in range(GlobalConst.MAX_STRESSTEST_CELL_SPACE):
	idx += 1
	datas[idx] = copy.deepcopy(cellspace)

	b += r					#累积一个角度
	x = a * math.cos( b ) 	# 半径 * 正余玄
	z = a * math.sin( b )
				
	datas[1].append((40001004, (x,  1.5, z),(0.0,0.0,0.0), 1, idx))
