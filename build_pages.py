import json, os

OUT = "/sessions/intelligent-focused-shannon/mnt/outputs"

memories = {
 "paris":      dict(title="巴黎", quote="[这一站最难忘的一句话]", story="巴黎圣母院的玫瑰花窗、歌剧院里镀金穹顶下的圣诞树、还有一顿地道的牛排薯条——这里的浪漫，一半来自建筑，一半来自味蕾。", photos=[f"photos/paris/paris-{i:02d}.jpg" for i in range(1,16)]),
 "iceland":    dict(title="雷克雅未克", quote="[这一站最难忘的一句话]", story="冰洞里啃一块透亮的冰、钻石沙滩上捡起被海浪冲上岸的浮冰、再等一场把天空染成金黄色的日出——雷克雅未克周边的这几天，冷得清醒，美得不真实。", photos=[f"photos/iceland/iceland-{i:02d}.jpg" for i in range(1,13)]),
 "edinburgh":  dict(title="爱丁堡", quote="[这一站最难忘的一句话]", story="卡尔顿山顶吹着风比耶，山下是爱丁堡老城和远处的福斯湾——这座城市的美，得爬到高处才看得全。", photos=[f"photos/edinburgh/edinburgh-{i:02d}.jpg" for i in range(1,4)]),
 "bath":       dict(title="巴斯", quote="[这一站最难忘的一句话]", story="巴斯温泉站的老式站牌、小店试衣镜前戴上的鸭舌帽——比起罗马浴场，更记得的是这座乔治王风格小城慢悠悠的一下午。", photos=[f"photos/bath/bath-{i:02d}.jpg" for i in range(1,4)]),
 "cambridge":  dict(title="剑桥", quote="[这一站最难忘的一句话]", story="撑一支篙，从数学桥下滑过康河——剑桥的学院城，安静得像一张明信片。", photos=[f"photos/cambridge/cambridge-{i:02d}.jpg" for i in range(1,4)]),
 "morocco":    dict(title="马拉喀什", quote="[这一站最难忘的一句话]", story="马拉喀什的塔吉锅和薄荷茶摆满一桌，夜里又钻进撒哈拉，裹着红色头巾坐在沙丘上——从市集的喧闹到沙漠的寂静，一天之内切换了两个世界。", photos=[f"photos/morocco/morocco-{i:02d}.jpg" for i in range(1,22)]),
 "hungary":    dict(title="布达佩斯", quote="[这一站最难忘的一句话]", story="渔人堡上眺望多瑙河和布达佩斯的红顶老城，国会大厦的尖顶在河对岸——这一眼，值回整趟旅程。", photos=[f"photos/hungary/hungary-{i:02d}.jpg" for i in range(1,23)]),
 "santorini":  dict(title="圣托里尼", quote="[这一站最难忘的一句话]", story="邮轮停在圣托里尼的火山湾里，小艇突突突地把游客送上岸——比起想象中的蓝顶白墙，记忆最深的其实是那一片深得发蓝的海水。", photos=[f"photos/greece/santorini-{i:02d}.jpg" for i in range(1,14)]),
 "piraeus":    dict(title="比雷埃夫斯", quote="[这一站最难忘的一句话]", story="从比雷埃夫斯港口出发，一路到卫城看那几根撑了两千多年的石柱——雅典的阳光很直接，晒得人睁不开眼。", photos=[f"photos/greece/piraeus-{i:02d}.jpg" for i in range(1,18)]),
 "katakolon":  dict(title="卡塔科隆", quote="[这一站最难忘的一句话]", story="小小的港口小镇，是通往古奥林匹亚遗址和爱奥尼亚海边绝美海湾的跳板——最惊艳的一片海水，是从山崖上往下看到的。", photos=[f"photos/greece/katakolon-{i:02d}.jpg" for i in range(1,11)]),
 "corfu":      dict(title="科孚岛", quote="[这一站最难忘的一句话]", story="科孚岛的海水清澈得能看见脚下的鹅卵石，穿着裙子在浅滩边张开手臂——爱奥尼亚海的颜色，怎么拍都不够。", photos=[f"photos/greece/corfu-{i:02d}.jpg" for i in range(1,12)]),
 "barcelona":  dict(title="巴塞罗那", quote="[这一站最难忘的一句话]", story="烤到焦香的巴斯克芝士蛋糕，还有铺满番茄和布拉塔奶酪的早午餐——巴塞罗那的记忆，好像有一半都跟吃有关。", photos=[f"photos/barcelona/barcelona-{i:02d}.jpg" for i in range(1,13)]),
 "seville":    dict(title="塞维利亚", quote="[这一站最难忘的一句话]", story="花园喷泉边一只鸭子悠闲地散步，精致的马赛克拼贴在阳光下发亮——塞维利亚的慢，是刻在建筑和花园里的。", photos=[f"photos/seville/seville-{i:02d}.jpg" for i in range(1,17)]),
 "austria":    dict(title="奥地利", quote="[这一站最难忘的一句话]", story="城市公园里，鲜花摆成的音符和莫扎特的雕像相对而立，还有沃蒂夫教堂的双塔尖顶被灯光勾出一道无穷符号——不愧是音乐与生活美学之城。", photos=[f"photos/austria/austria-{i:02d}.jpg" for i in range(1,14)]),
 "czech":      dict(title="捷克", quote="[这一站最难忘的一句话]", story="老城广场上，圣母提恩教堂的双塔尖顶刺向天空，红白相间的老式电车沿着石板路缓缓驶过——布拉格的城市感，一半在建筑，一半在轨道上。", photos=[f"photos/czech/czech-{i:02d}.jpg" for i in range(1,10)]),
 "venice":     dict(title="威尼斯", quote="[这一站最难忘的一句话]", story="圣乔治马焦雷教堂对岸，贡多拉船夫撑着船缓缓划过，街边小店里一份炸海鲜拼盘用蓝色纸袋装着——威尼斯的水城感，吃的和看的都很足。", photos=[f"photos/venice/venice-{i:02d}.jpg" for i in range(1,8)]),
 "florence":   dict(title="佛罗伦萨", quote="[这一站最难忘的一句话]", story="夕阳把老桥染成金色，河面上波光粼粼，晚饭是一大盘意面配着墙上的老肖像画——文艺复兴之城的浪漫，饭桌上也能感受到。", photos=[f"photos/florence/florence-{i:02d}.jpg" for i in range(1,10)]),
 "rome":       dict(title="罗马", quote="[这一站最难忘的一句话]", story="万神殿前的方尖碑刺向蓝天，图拉真柱旁的古罗马广场废墟在夕阳里泛着暖色——罗马的伟大，走在路上就能撞见。", photos=[f"photos/rome/rome-{i:02d}.jpg" for i in range(1,15)]),
 "portugal":   dict(title="里斯本", quote="[这一站最难忘的一句话]", story="涂满涂鸦的黄色老电车哼哧哼哧爬上里斯本的坡道，热罗尼莫斯修道院的石雕精致得让人挪不开脚——里斯本，是电车轨道和修道院石头共同写成的故事。", photos=[f"photos/portugal/portugal-{i:02d}.jpg" for i in range(1,15)]),
 "london":     dict(title="伦敦", quote="[这一站最难忘的一句话]", story="国家美术馆里一幅古典油画、老餐厅门口咬一口刚买的司康饼、还有和朋友挤在快照亭里做鬼脸——伦敦的日常，博物馆和街角小店各占一半。", photos=[f"photos/london/london-{i:02d}.jpg" for i in range(1,27)]),
}

order = ["paris","iceland","edinburgh","bath","cambridge","morocco","hungary",
         "santorini","piraeus","katakolon","corfu","barcelona","seville",
         "austria","czech","venice","florence","rome","portugal","london"]

locations = {
 "paris":(48.8566,2.3522,"巴黎"), "iceland":(64.1466,-21.9426,"雷克雅未克"),
 "edinburgh":(55.9533,-3.1883,"爱丁堡"), "bath":(51.3811,-2.3590,"巴斯"),
 "cambridge":(52.2053,0.1218,"剑桥"), "morocco":(31.6295,-7.9811,"马拉喀什"),
 "hungary":(47.4979,19.0402,"布达佩斯"), "santorini":(36.3932,25.4615,"圣托里尼"),
 "piraeus":(37.9475,23.6360,"比雷埃夫斯"), "katakolon":(37.6500,21.3167,"卡塔科隆"),
 "corfu":(39.6243,19.9217,"科孚岛"), "barcelona":(41.3851,2.1734,"巴塞罗那"),
 "seville":(37.3891,-5.9845,"塞维利亚"), "austria":(48.2082,16.3738,"奥地利"),
 "czech":(50.0755,14.4378,"捷克"), "venice":(45.4408,12.3155,"威尼斯"),
 "florence":(43.7696,11.2558,"佛罗伦萨"), "rome":(41.9028,12.4964,"罗马"),
 "portugal":(38.7223,-9.1393,"里斯本"), "london":(51.5074,-0.1278,"伦敦"),
}

CSS = """:root{
  --ink:#1c1c1c;
  --paper:#faf8f5;
  --paper-dim:#f1ede7;
  --line:#d8d2c8;
  --accent:#b5673a;
  --muted:#7a756c;
}
*{box-sizing:border-box;margin:0;padding:0;}
body{
  font-family:"Helvetica Neue", "PingFang SC", "Microsoft YaHei", sans-serif;
  background:var(--paper);
  color:var(--ink);
  line-height:1.7;
}
a{color:inherit;text-decoration:none;}

/* ---------- 封面 ---------- */
.cover{
  min-height:60vh;
  display:flex; flex-direction:column;
  justify-content:center; align-items:flex-start;
  padding:8vh 8vw;
  border-bottom:1px solid var(--line);
}
.cover .eyebrow{
  font-size:13px; letter-spacing:3px; text-transform:uppercase;
  color:var(--accent); margin-bottom:18px;
}
.cover h1{
  font-size:clamp(2.2rem, 6vw, 4.2rem);
  font-weight:300;
  line-height:1.15;
  margin-bottom:20px;
}
.cover h1 em{ font-style:normal; color:var(--accent); }
.cover .meta{
  font-size:13px; color:var(--muted); letter-spacing:0.5px;
}

/* ---------- 地图区 ---------- */
.map-section{
  padding:9vh 6vw 11vh;
  text-align:center;
  border-bottom:1px solid var(--line);
  background:var(--paper-dim);
}
.map-section .eyebrow{
  font-size:13px; letter-spacing:3px; text-transform:uppercase;
  color:var(--accent); margin-bottom:14px;
}
.map-section h2{
  font-size:clamp(1.6rem, 4vw, 2.4rem);
  font-weight:300; margin-bottom:10px;
}
.map-section .hint{
  font-size:13px; color:var(--muted); margin-bottom:36px;
}
.map-wrap{
  max-width:920px; margin:0 auto;
  position:relative;
}
#map{
  height:600px;
  border-radius:10px;
  border:1px solid var(--line);
  box-shadow:0 10px 30px rgba(0,0,0,.08);
  background:var(--paper-dim);
}
#map .leaflet-tile-pane{
  filter:saturate(0.55) sepia(0.12) brightness(1.03);
}
.map-pin{ position:relative; width:18px; height:18px; cursor:pointer; }
.map-pin .dot{
  position:absolute; top:5px; left:5px; width:8px; height:8px; border-radius:50%;
  background:var(--accent); border:2px solid var(--paper);
  box-shadow:0 1px 3px rgba(0,0,0,.3);
}
.map-pin .ring{
  position:absolute; top:1px; left:1px; width:16px; height:16px; border-radius:50%;
  border:1.4px solid var(--accent); opacity:.6;
  animation:pulse 2.6s ease-out infinite;
}
@keyframes pulse{
  0%{ transform:scale(0.5); opacity:.6; }
  100%{ transform:scale(2.2); opacity:0; }
}
.leaflet-tooltip.city-tooltip{
  background:transparent; border:none; box-shadow:none;
  font-size:11.5px; font-weight:600; color:var(--ink);
  text-shadow:
    -1px -1px 0 var(--paper-dim), 1px -1px 0 var(--paper-dim),
    -1px 1px 0 var(--paper-dim), 1px 1px 0 var(--paper-dim),
    0 0 5px var(--paper-dim);
  padding:0;
}
.leaflet-tooltip.city-tooltip::before{ display:none; }
@media (max-width:640px){
  #map{ height:420px; }
}

/* ---------- 收尾 ---------- */
.closing{
  padding:14vh 8vw; text-align:center;
  background:var(--ink); color:var(--paper);
}
.closing h2{ font-size:clamp(1.6rem, 4vw, 2.4rem); font-weight:300; max-width:700px; margin:0 auto; }

/* ---------- 城市详情页 ---------- */
.detail-topbar{
  padding:22px 8vw;
  border-bottom:1px solid var(--line);
}
.detail-topbar .back-link{
  font-size:13px; color:var(--muted); letter-spacing:0.5px;
}
.detail-topbar .back-link:hover{ color:var(--accent); }
.detail-header{
  padding:8vh 8vw 5vh;
  border-bottom:1px solid var(--line);
}
.detail-header h1{
  font-size:clamp(2rem, 5vw, 3.4rem);
  font-weight:300;
  margin-bottom:24px;
}
.detail-quote{
  border-left:3px solid var(--accent); padding-left:18px;
  font-size:1.15rem; font-weight:300; color:#3a3a3a;
  max-width:640px;
}
.detail-story{
  padding:5vh 8vw 2vh;
  max-width:720px;
  font-size:1rem; color:#3a3a3a;
}
.detail-gallery{
  padding:3vh 0 10vh 8vw;
  display:flex;
  gap:18px;
  overflow-x:auto;
  overflow-y:hidden;
  scroll-snap-type:x mandatory;
  -webkit-overflow-scrolling:touch;
  scrollbar-width:thin;
  scrollbar-color:var(--line) transparent;
}
.detail-gallery::after{
  content:"";
  flex:0 0 8vw;
}
.detail-gallery::-webkit-scrollbar{ height:6px; }
.detail-gallery::-webkit-scrollbar-thumb{ background:var(--line); border-radius:3px; }
.detail-gallery::-webkit-scrollbar-track{ background:transparent; }
.detail-gallery img{
  height:70vh; max-height:560px; width:auto; max-width:85vw;
  display:block; border-radius:8px; flex:0 0 auto;
  scroll-snap-align:center;
  box-shadow:0 8px 24px rgba(0,0,0,.12);
}
@media (max-width:640px){
  .detail-gallery img{ height:56vh; }
}
.detail-nav{
  display:flex; justify-content:space-between;
  padding:5vh 8vw 10vh;
  border-top:1px solid var(--line);
  font-size:13px; color:var(--muted);
}
.detail-nav a:hover{ color:var(--accent); }

@media (max-width:640px){
  .cover, .map-section, .closing, .detail-topbar, .detail-header, .detail-story, .detail-gallery, .detail-nav{
    padding-left:6vw; padding-right:6vw;
  }
}
"""

with open(os.path.join(OUT, "style.css"), "w", encoding="utf-8") as f:
    f.write(CSS)

def render_gallery(photos):
    return "\n".join(f'    <img src="{p}" alt="">' for p in photos)

PAGE_TMPL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · 留学时光</title>
<link rel="stylesheet" href="style.css">
</head>
<body>

<div class="detail-topbar">
  <a class="back-link" href="study-abroad-memories-demo.html">← 返回地图</a>
</div>

<header class="detail-header">
  <h1>{title}</h1>
</header>

<div class="detail-story">{story}</div>

<div class="detail-gallery">
{gallery}
</div>

<div class="detail-nav">
  <a href="{prev}.html">← {prev_label}</a>
  <a href="{next}.html">{next_label} →</a>
</div>

</body>
</html>
"""

n = len(order)
for i, cid in enumerate(order):
    m = memories[cid]
    prev_id = order[(i-1) % n]
    next_id = order[(i+1) % n]
    html = PAGE_TMPL.format(
        title=m["title"],
        quote=m["quote"],
        story=m["story"],
        gallery=render_gallery(m["photos"]),
        prev=prev_id, prev_label=memories[prev_id]["title"],
        next=next_id, next_label=memories[next_id]["title"],
    )
    with open(os.path.join(OUT, f"{cid}.html"), "w", encoding="utf-8") as f:
        f.write(html)

print("Generated style.css and", len(order), "detail pages")
