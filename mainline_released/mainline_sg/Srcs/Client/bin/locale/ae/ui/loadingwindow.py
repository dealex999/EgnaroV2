import uiScriptLocale

window = {
	"name" : "LoadingWindow",
	"sytle" : ("movable","ltr",),

	"x" : 0,
	"y" : 0,

	"width" : SCREEN_WIDTH,
	"height" : SCREEN_HEIGHT,

	"children" :
	(
		## Board
		{
			"name" : "BackGround",
			"type" : "expanded_image",

			"x" : 0,
			"y" : 0,

			"image" : "d:/ymir work/uiloading/background_loading_warrior.sub",

			"x_scale" : float(SCREEN_WIDTH) / 800.0,
			"y_scale" : float(SCREEN_HEIGHT) / 600.0,
		},
		{ 
			"name":"ErrorMessage", 
			"type":"text", "x":10, "y":10, 
			"text": uiScriptLocale.LOAD_ERROR, 
		},
		{
			"name" : "GageBoard",
			"type" : "window",
			"x" : float(SCREEN_WIDTH) * 250 / 800.0,
			"y" : float(SCREEN_HEIGHT) * 500 / 600.0 ,
			"width" : 400, 
			"height": 80,

			"children" :
			(
				{
					"name" : "BackGage",
					"type" : "ani_image",


					"x" : 405,
					"y" : 0,

					"delay" : 1,

					"images" :
					(
						"d:/ymir work/ui/intro/loading/00.sub",
						"d:/ymir work/ui/intro/loading/01.sub",
						"d:/ymir work/ui/intro/loading/02.sub",
						"d:/ymir work/ui/intro/loading/03.sub",
						"d:/ymir work/ui/intro/loading/04.sub",
						"d:/ymir work/ui/intro/loading/05.sub",
						"d:/ymir work/ui/intro/loading/06.sub",
						"d:/ymir work/ui/intro/loading/07.sub",
						"d:/ymir work/ui/intro/loading/08.sub",
						"d:/ymir work/ui/intro/loading/09.sub",
						"d:/ymir work/ui/intro/loading/10.sub",
						"d:/ymir work/ui/intro/loading/11.sub",						
						"d:/ymir work/ui/intro/loading/12.sub",
						"d:/ymir work/ui/intro/loading/13.sub",
						"d:/ymir work/ui/intro/loading/14.sub",
						"d:/ymir work/ui/intro/loading/15.sub",
						"d:/ymir work/ui/intro/loading/16.sub",
						"d:/ymir work/ui/intro/loading/17.sub",
						"d:/ymir work/ui/intro/loading/18.sub",
						"d:/ymir work/ui/intro/loading/19.sub",
						"d:/ymir work/ui/intro/loading/20.sub",
						"d:/ymir work/ui/intro/loading/21.sub",
						"d:/ymir work/ui/intro/loading/22.sub",
						"d:/ymir work/ui/intro/loading/23.sub",
					)
				},
				{
					"name" : "BackGage",
					"type" : "expanded_image",

					"x" : 0,
					"y" : 25,

					"image" : "d:/ymir work/ui/intro/loading/gauge_empty.sub",			
				},
				{
					"name" : "FullGage",
					"type" : "expanded_image",

					"x" : 0,
					"y" : 25,

					"image" : "d:/ymir work/ui/intro/loading/gauge_full.sub",			
				},
			),
		},
	),
}
