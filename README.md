# A Dianping.com Spider based on users
Preparation for installing:
- python3.5
- beautifulsoup4
- re
- lxml

You can use *pip install* to install the required components after successfully installed python3.5

Email modules is prepared for your need

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