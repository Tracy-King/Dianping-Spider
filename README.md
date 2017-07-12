# A Dianping.com Spider based on users

update v2.0 on 7.12
New features:
- Set a threshold to filter those whose reviews number is less than the threshold
- Set a *verbose* flag for users to choose whether to records the personal info of those whose reviews number is under the threshold. *verbose == True* for yes and *verbose == False* for no.
- You can set the variable *startUid*, *endUid*, *threshold* at the beginning of the program, making it more convenient to user
- Get rid of the SSL certification of https website, only for users whose OS is too old or didn't install MS update for a long time
- Optimize the program structure, output info. Annotation has been added to every functions so that it's easy for you to understand
- *Data* folders and *Data/User* folders have been prepared for users to eliminate the error at first running

The only thing you need to do before running the program is to set four varibles: *startUid*, *endUid*, *verbose* and *threshold* at the beginning of the program.



------------------------------------------
Preparation for installing:
- python3.5
- beautifulsoup4
- re
- lxml

You can use *pip install* to install the required components after successfully installing python3.5

Email modules is prepared for your need

The program is able to save the data in time. So if there is any problem causing a idle, please feel free to kill the program and restart from where the idle happened

Users' personal information collected in default is:
- User Name
- User ID
- Icon Picture type (1 for customized icon, 0 for default icon)
- Register Time
- Review Number
- Wishlist Number
- Checkin Number
- Photos Number
- Mylist Number
- Groups Number
- Follows Number
- Fans Number
- Living Place*
- Contribution Value
- Love Status*
- Birthday*
- Constellation*
(* means if exists)

ex.:{UserName: 九指,	UserId: 1,	IconPic: 1,	RegisterTime: 20030417,	ReviewNum: 428,	WishlistNum: 127,	CheckinNum: 36,	PhotosNum: 211,	MylistNum: 211,	GroupsNum: 17,	FollowsNum: 838,	FansNum: 5917,	Place: None,	Contribution: 1682,	loveStatus:  ,	birthday: 1972-11-3,	constellation:  天蝎座}

User's review information collected in default is:
- Shop ID
- Shop Address
- Rank Star
- Average Price*
- Like
- Comment
- Picture Number
- Recommended Dishes*
- Time
(* means if exists)

ex.:{ShopNum: 500126,	ShopAddr: 南京西路1728号百乐门20楼,	ShopStar: -1,	AvgPrice: -1,	Like: 0,	Comment: [不错的好地方., ],	PictureNum: 0,	Dishes: [粉条, ],	Time: 030425}
