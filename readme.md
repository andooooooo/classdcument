# ABOUT
タグ付けされた大量の英語文書データを元にナイーブベイズで分類器を作成し、入力文書を分類する。<br/>
# METHOD
まず、訓練データを<br/>
<document><br/>
	<ID>識別ID</ID><br/>
	<cat>カテゴリー名</cat><br/>
	<body>内容</body><br/>
</document><br/>
のようにタグ付けする<br/>
次に、単語間のスペースで区切り、一行に一単語のtxtを作る<br/>
clean.pyを実行すると、カンマなどが取り除かれて、各Documentが【カテゴリー名.txt】のように分けられて、カテゴリーの分類確率が算出される。（このコードでは５つのカテゴリーを想定している）<br/>
classfication.pyにその分類確率を入れて実行するとresult.txtにIDとともに分類されたカテゴリー名が記述される<br/>
また、入力文書は次のようにタグを付与する
<document><br/>
	<ID>識別ID</ID><br/>
	<cat></cat><br/>
	<body>内容</body><br/>
</document><br/>
