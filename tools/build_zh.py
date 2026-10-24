"""Generate index.zh.html from index.html by exact text replacements (each must match the expected count).

Run after editing index.html:  python tools/build_zh.py
If an English string changed, the script stops and names it; update its entry in R and run again.
"""
import sys
from pathlib import Path

site = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
s = (site / "index.html").read_text(encoding="utf-8")


def keep(*phrases):
    """Each phrase wraps as a unit, so a line never breaks inside one."""
    return "".join(f'<span style="display:inline-block">{p}</span>' for p in phrases)


# (english, chinese, expected count)
R = [
    ('<html lang="en">', '<html lang="zh-CN">', 1),
    ('<title>CS2 World Model</title>', '<title>CS2 World Model · 中文</title>', 1),
    ('content="From esports data to a multi-player interactive world model: the CS2 World Model and the Esports World Model Dataset."',
     'content="从电竞数据出发，构建多人交互的世界模型：CS2 世界模型与电竞世界模型数据集。"', 1),
    # nav
    ('<a class="lang" href="index.zh.html" hreflang="zh-CN" lang="zh-CN">中文</a>',
     '<a class="lang" href="index.html" hreflang="en" lang="en">EN</a>', 1),
    ('<a href="#pipeline">Overview</a><a href="#compare">Compare</a><a href="#overview">Method</a><a href="#results">Seven maps</a>',
     '<a href="#pipeline">总览</a><a href="#compare">真假对比</a><a href="#overview">核心能力</a><a href="#results">七图实测</a>', 1),
    ('<a href="#multiplayer">Multi-player</a><a href="#dataset">Dataset</a><a href="#citation">Citation</a>',
     '<a href="#multiplayer">多人</a><a href="#dataset">数据集</a><a href="#citation">引用</a>', 1),
    # hero
    ('<i></i>Every frame in the background is generated</span>', '<i></i>背景画面，全部由模型生成</span>', 1),
    ('From esports data to a multi-player interactive world model: one model renders every player of a Counter-Strike&nbsp;2 round.',
     keep('从电竞数据出发，', '构建多人交互的世界模型。') + '<br>' + keep('一个模型，', '生成整局 CS2 的每一名选手。'), 1),
    ('<span class="badge">World first</span>', '<span class="badge">全球首个</span>', 4),
    ('<strong>Full 5v5 world model</strong><span>All ten players of both teams generated together, consistent across every view.</span>',
     '<strong>完整 5v5 对局的世界模型</strong><span>双方十名选手同时生成，每个视角严丝合缝。</span>', 1),
    ('<strong>Multi-player combat world model</strong><span>Firefights and kills between players, on maps that stay consistent.</span>',
     '<strong>真实多人对抗的世界模型</strong><span>选手之间交火、击杀，地图始终保持一致。</span>', 1),
    ('<strong>720p &middot; 32&nbsp;fps multi-player FPS world model</strong><span>Multi-player shooter world models reach 720p and 32&nbsp;fps for the first time.</span>',
     '<strong>720p &middot; 32 帧多人射击世界模型</strong><span>多人射击世界模型首次达到这一画质。</span>', 1),
    ('<strong>Data&ndash;model closed-loop esports world model</strong><span>Pro-player collection, cleaning, alignment, training and evaluation, all built in-house.</span>',
     '<strong>数据与模型闭环的电竞世界模型</strong><span>职业选手采集、清洗对齐、模型训练到评测补采，全流程自研。</span>', 1),
    ('<p class="caps">One model &middot; 7 maps &middot; both sides &middot; every weapon</p>',
     '<p class="caps">一个模型 &middot; 七张地图 &middot; 双方阵营 &middot; 全部武器</p>', 1),
    # overview
    ('<p class="kicker reveal">Overview</p>', '<p class="kicker reveal">总览</p>', 1),
    ('<h2 class="reveal">From data to world model, one closed loop</h2>', '<h2 class="reveal">从数据到世界模型，完整闭环</h2>', 1),
    ("We built every stage ourselves: pro players record real matches, the recordings are cleaned and aligned frame by frame with actions and game state, and the aligned data trains one world model.",
     "每一环都由我们自己完成：职业选手录制真实对局，画面与操作、游戏状态逐帧清洗对齐，再用来训练同一个世界模型。", 1),
    ("<li><b>01</b><strong>Collect</strong><span>Pro players, every player's first-person view</span></li>",
     "<li><b>01</b><strong>职业选手采集</strong><span>真实对局，全员第一视角</span></li>", 1),
    ("<li><b>02</b><strong>Clean &amp; align</strong><span>Video, actions and game state, frame by frame</span></li>",
     "<li><b>02</b><strong>清洗与对齐</strong><span>画面、操作、游戏状态逐帧对齐</span></li>", 1),
    ("<li><b>03</b><strong>Train</strong><span>One world model for all seven maps</span></li>",
     "<li><b>03</b><strong>世界模型训练</strong><span>一个模型覆盖七张地图</span></li>", 1),
    ("<li><b>04</b><strong>Evaluate</strong><span>Compare with real recordings, find the gaps</span></li>",
     "<li><b>04</b><strong>生成评测</strong><span>与真实录像逐段对比，定位缺陷</span></li>", 1),
    ("Whatever the model is missing, we go and collect: data and model improve together.",
     "模型缺什么数据，就定向采集什么：数据与模型共同迭代。", 1),
    ('<span class="part-no">Part 1</span>', '<span class="part-no">第一部分</span>', 1),
    ('<span class="part-no">Part 2</span>', '<span class="part-no">第二部分</span>', 1),
    ('<h3>CS2 World Model</h3>', '<h3>CS2 世界模型</h3>', 1),
    ("<p>Generates each player's first-person view from the match, with all ten players in the same world.</p>",
     "<p>根据对局生成每名选手的第一视角画面，十人同处一个世界，交火、击杀一应俱全。</p>", 1),
    ('<li><b>10</b>players at once</li><li><b>7</b>maps, one model</li><li><b>720p</b>at 32 fps</li>',
     '<li><b>10</b>名选手同时生成</li><li><b>7</b>张地图，一个模型</li><li><b>720p</b>32 帧/秒</li>', 1),
    ('<span class="go">Watch results &rarr;</span>', '<span class="go">观看演示 &rarr;</span>', 1),
    ('<h3>Esports World Model Dataset</h3>', '<h3>电竞世界模型数据集</h3>', 1),
    ("<p>Real matches in StarCraft&nbsp;II, Dota&nbsp;2 and CS2, every player's view aligned with actions, state and events.</p>",
     "<p>星际争霸&nbsp;II、Dota&nbsp;2、CS2 的真实对局，每名选手的画面都与操作、状态和事件对齐。</p>", 1),
    ('<li><b>2,673</b>matches</li><li><b>~3,828&nbsp;h</b>player views</li><li><b>3</b>games</li>',
     '<li><b>2,673</b>场对局</li><li><b>~3,828</b>小时选手视角</li><li><b>3</b>款游戏</li>', 1),
    ('<span class="go">Explore the dataset &rarr;</span>', '<span class="go">浏览数据集 &rarr;</span>', 1),
    ('<p class="part reveal">Part 1 &middot; CS2 World Model</p>', '<p class="part reveal">第一部分 &middot; CS2 世界模型</p>', 1),
    ('<p class="part reveal">Part 2 &middot; Esports World Model Dataset</p>', '<p class="part reveal">第二部分 &middot; 电竞世界模型数据集</p>', 1),
    ('<span><sup>1</sup>KAUST</span><span><sup>2</sup>Institute of Automation, Chinese Academy of Sciences</span><span><sup>3</sup>Beijing Zhongguancun Academy</span>',
     '<span><sup>1</sup>阿卜杜拉国王科技大学（KAUST）</span><span><sup>2</sup>中国科学院自动化研究所</span><span><sup>3</sup>北京中关村学院</span>', 1),
    ('</svg>Watch results</a>', '</svg>观看演示</a>', 1),
    ('<a class="btn ghost" href="#dataset">Dataset</a>', '<a class="btn ghost" href="#dataset">数据集</a>', 1),
    ('<a class="btn ghost" href="https://arxiv.org/abs/2610.16166">Dataset paper</a>',
     '<a class="btn ghost" href="https://arxiv.org/abs/2610.16166">数据集论文</a>', 1),
    ('<div class="scroll-cue">Scroll</div>', '<div class="scroll-cue">向下滑动</div>', 1),
    # compare
    ('<p class="kicker reveal">Real vs. generated</p>', '<p class="kicker reveal">以假乱真</p>', 1),
    ('<h2 class="reveal">Drag to compare</h2>', '<h2 class="reveal">哪一边是真的？</h2>', 1),
    ('Left of the handle is the original recording; right of it is our model. Starting from the opening frames and the match state, the model renders the next eight seconds at 720p and 32&nbsp;fps.',
     '左边是职业比赛录像，右边由模型生成。只需开局几帧和对局数据，即可续写 8 秒 720p 高清画面。拖动滑块，自己来分辨。', 1),
    ('<span class="slider-label l">Real</span><span class="slider-label r">Generated</span>',
     '<span class="slider-label l">录像</span><span class="slider-label r">生成</span>', 1),
    ('<span>de_overpass &middot; walking into bombsite A</span><span>Held-out validation round</span>',
     '<span>de_overpass &middot; 摸进 A 点</span><span>训练中从未出现过的回合</span>', 1),
    # method
    ('<p class="kicker reveal">Method</p>', '<p class="kicker reveal">核心能力</p>', 1),
    ('<h2 class="reveal">Rendering from the game state</h2>', '<h2 class="reveal">懂地图，懂对局，懂视角</h2>', 1),
    ("""      Given where a player stands and looks, what everyone in the round is doing, and the map being played,
      the model renders what that player sees. Map structure, lighting and materials stay consistent as the
      camera moves through rooms and across levels.""",
     """      选手站在哪、看向哪，场上十人在做什么，正在打哪张图——模型全都了然于胸，并据此画出选手此刻所见。穿廊过道、跨越楼层、转身回看，场景始终严丝合缝。""", 1),
    ('<h3>Map-aware</h3><p>The model knows all seven maps by heart, so walls, doors and skylines stay exactly where the map puts them, however the camera turns.</p>',
     '<h3>吃透地图</h3><p>七张职业地图烂熟于心。墙体、门洞、掩体分毫不差，视角怎么转都不穿帮。</p>', 1),
    ('<h3>Full game state</h3><p>All ten players are part of the scene: who is where, and what they are doing, shows up correctly in every view.</p>',
     '<h3>掌控全局</h3><p>十名选手尽在掌握。谁在哪、在做什么，每一个画面都与真实对局一一对应。</p>', 1),
    ('<h3>Seven maps</h3><p>Ancient, Anubis, Dust&nbsp;II, Inferno, Mirage, Nuke and Overpass, at 720p and 32&nbsp;fps.</p>',
     '<h3>七图全覆盖</h3><p>Ancient、Anubis、Dust&nbsp;II、Inferno、Mirage、Nuke、Overpass，一张不落。</p>', 1),
    ('<h3>Video backbone</h3><p>Fine-tuned from Cosmos3-Nano with the Wan2.2 VAE; an eight-second window is denoised jointly.</p>',
     '<h3>大模型底座</h3><p>基于 Cosmos3-Nano 微调，搭配 Wan2.2 VAE，8 秒画面一气呵成。</p>', 1),
    ('aria-label="Model overview"', 'aria-label="模型概览"', 1),
    ('<div class="chip"><b></b>Map</div>', '<div class="chip"><b></b>地图</div>', 1),
    ('<div class="chip"><b></b>Match state</div>', '<div class="chip"><b></b>对局数据</div>', 1),
    ('<strong>Video world model</strong><span>Cosmos3-Nano backbone</span>',
     '<strong>视频世界模型</strong><span>Cosmos3-Nano 底座</span>', 1),
    ('<strong>First-person video</strong>', '<strong>第一视角画面</strong>', 1),
    # seven maps
    ('<p class="kicker reveal">Results</p>', '<p class="kicker reveal">效果展示</p>', 1),
    ('<h2 class="reveal">Seven maps</h2>', '<h2 class="reveal">七张地图，逐一实测</h2>', 1),
    ('Left: the original recording. Right: our rendering of the same eight seconds, at 1280&times;720. All clips come from held-out validation rounds. Switch to a single view or open a clip full screen to see it at full resolution.',
     '左为职业比赛录像，右为模型生成，1280&times;720 原画呈现。所有片段均来自训练中从未出现的回合。切换单画面或全屏，细节一览无余。', 1),
    ('aria-label="Map filter"', 'aria-label="按地图筛选"', 1),
    ('aria-label="View mode"', 'aria-label="显示方式"', 1),
    ('<button type="button" data-view="both" aria-pressed="true">Side by side</button>',
     '<button type="button" data-view="both" aria-pressed="true">左右对比</button>', 1),
    ('<button type="button" data-view="gen" aria-pressed="false">Generated only</button>',
     '<button type="button" data-view="gen" aria-pressed="false">只看生成</button>', 2),
    ('<button type="button" data-view="real" aria-pressed="false">Real only</button>',
     '<button type="button" data-view="real" aria-pressed="false">只看录像</button>', 2),
    # multi-player
    ('<p class="kicker reveal">Multi-player</p>', '<p class="kicker reveal">多人</p>', 1),
    ('<h2 class="reveal">Several players, one moment</h2>', '<h2 class="reveal">多个视角，同一个战场</h2>', 1),
    ('All players in a round share one game state. Each view below is generated separately, yet they agree: the same wall, the same opponent, seen through different eyes.',
     '同一回合，每名选手的画面分别生成，却能彼此呼应：同一面墙、同一个对手，换个角度看过去，依然严丝合缝。', 1),
    ('aria-label="Multi-player mode"', 'aria-label="多人显示方式"', 1),
    ('<button type="button" data-view="both" aria-pressed="true">Real &amp; generated</button>',
     '<button type="button" data-view="both" aria-pressed="true">录像与生成</button>', 1),
    ('<div class="mv-half real"><span class="mv-row">Real</span></div>', '<div class="mv-half real"><span class="mv-row">录像</span></div>', 1),
    ('<div class="mv-half gen"><span class="mv-row">Generated</span></div>', '<div class="mv-half gen"><span class="mv-row">生成</span></div>', 1),
    ('aria-label="Seek"', 'aria-label="进度"', 1),
    ('aria-label="Players per round"', 'aria-label="按人数筛选"', 1),
    ('Click the video to pause &middot; press and hold to flash the real views',
     '点击画面暂停 &middot; 长按画面查看录像', 1),
    ("Held-out validation rounds, 1280&times;720 per view at 32&nbsp;fps for eight seconds (shown at half size). T and CT mark each player's side.",
     '全部来自训练中从未出现的回合。每个视角 1280&times;720、32 帧、8 秒，页面按一半尺寸显示；T、CT 为选手阵营。', 1),
    # dataset
    ('<p class="kicker reveal">Dataset</p>', '<p class="kicker reveal">开源数据集</p>', 1),
    ('<h2 class="reveal">Esports World Model Dataset</h2>', '<h2 class="reveal">电竞世界模型数据集</h2>', 1),
    ("""          Replays of real players decoded into multi-player videos for StarCraft&nbsp;II, Dota&nbsp;2 and
          Counter-Strike&nbsp;2, time-aligned with game actions, engine state and events. Built for action-conditioned
          world models, multi-player consistency, partial observability and video understanding.""",
     """          2,673 场真实对局，约 3,828 小时选手第一视角视频，横跨星际争霸&nbsp;II、Dota&nbsp;2、CS2 三大电竞项目。每一帧画面都与选手操作、游戏状态和比赛事件精确对齐，为世界模型、多人视角理解等研究提供真实素材。""", 1),
    ('<div class="lbl">matches</div>', '<div class="lbl">场真实对局</div>', 1),
    ('<div class="lbl">player-view hours</div>', '<div class="lbl">小时选手视角视频</div>', 1),
    ('<div class="lbl">games: RTS, MOBA, FPS</div>', '<div class="lbl">大电竞项目：RTS、MOBA、FPS</div>', 1),
    ('<div class="lbl">downloads on ModelScope</div>', '<div class="lbl">次魔搭下载</div>', 1),
    ('>Download on ModelScope</a>', '>前往魔搭下载</a>', 1),
    ('>Documentation</a>', '>使用文档</a>', 1),
    ('>arXiv paper</a>', '>arXiv 论文</a>', 1),
    ('<span class="live"><i></i>Player view</span>', '<span class="live"><i></i>第一视角</span>', 3),
    ('aria-label="StarCraft II player view"', 'aria-label="星际争霸 II 选手视角"', 1),
    ('aria-label="Dota 2 player view"', 'aria-label="Dota 2 选手视角"', 1),
    ('aria-label="Counter-Strike 2 player view"', 'aria-label="CS2 选手视角"', 1),
    ('<h3>StarCraft II</h3>', '<h3>星际争霸 II</h3>', 1),
    ('<h3>Counter-Strike 2</h3>', '<h3>CS2</h3>', 1),
    ('<dt>Matches</dt>', '<dt>对局数</dt>', 3),
    ('<dt>Gameplay</dt>', '<dt>对局时长</dt>', 3),
    ('<dt>Player views</dt>', '<dt>视角时长</dt>', 3),
    ('<dt>Views</dt>', '<dt>视角</dt>', 3),
    ('<dt>Structured</dt>', '<dt>结构化数据</dt>', 3),
    ('395.8 h', '395.8 小时', 1), ('791.5 h', '791.5 小时', 1), ('195.5 h', '195.5 小时', 1),
    ('1,955.0 h', '1,955.0 小时', 1), ('34.8 h', '34.8 小时', 1), ('138.4 h', '138.4 小时', 1),
    ('<dd>2 per match</dd>', '<dd>每场双方 2 个</dd>', 1),
    ('<dd>~59M trajectory steps</dd>', '<dd>约 5900 万轨迹步</dd>', 1),
    ('<dd>up to 10 per match</dd>', '<dd>每场最多 10 个</dd>', 1),
    ('<dd>~7.7B state changes, 220M events</dd>', '<dd>约 77 亿次状态变化、2.2 亿个事件</dd>', 1),
    ('<dd>7,623 round POV clips</dd>', '<dd>7,623 段回合视角</dd>', 1),
    ('<dd>64 tick/s state, 16 fps video</dd>', '<dd>状态 64 tick/秒，视频 16 帧</dd>', 1),
    # games in collection
    ('<h3>Coming next: 20+ popular games</h3>', '<h3>即将加入：20 余款热门游戏</h3>', 1),
    ('<p>Data collection is under way for more titles. They are not part of the current release.</p>',
     '<p>更多热门游戏正在加紧采集，暂未包含在当前发布的数据集中。</p>', 1),
    ('<span class="collect-tag"><i></i>Collecting</span>', '<span class="collect-tag"><i></i>采集中</span>', 1),
    ('<b>Valorant</b>', '<b>无畏契约</b>', 1),
    ('<b>League of Legends</b>', '<b>英雄联盟</b>', 1),
    ('<b>Delta Force</b>', '<b>三角洲行动</b>', 1),
    ('<b>Age of Empires II</b>', '<b>帝国时代 II</b>', 1),
    ('<b>Age of Empires IV</b>', '<b>帝国时代 IV</b>', 1),
    ('<h3>Every player, the same moment</h3>', '<h3>同一瞬间，全员视角</h3>', 1),
    ('<p>Real replays decoded per player and lined up on the replay clock. Pick a game:</p>',
     '<p>真实录像逐人解码、逐帧对齐，同一时刻的每个视角尽收眼底。</p>', 1),
    ('aria-label="Game"', 'aria-label="游戏"', 1),
    ('>StarCraft&nbsp;II &middot; 2 views</button>', '>星际争霸&nbsp;II &middot; 双方视角</button>', 1),
    ('>Dota&nbsp;2 &middot; 10 views</button>', '>Dota&nbsp;2 &middot; 十人视角</button>', 1),
    ('>Counter-Strike&nbsp;2 &middot; 10 views</button>', '>CS2 &middot; 十人视角</button>', 1),
    ('<h3 class="reveal">Trailer</h3>', '<h3 class="reveal">宣传片</h3>', 1),
    ('<h3>License</h3>', '<h3>许可</h3>', 1),
    ('<li>Non-commercial research use only; our decoded data, metadata and scripts are released under CC BY-NC 4.0.</li>',
     '<li>仅限非商业研究使用；我们解码的数据、元数据和脚本以 CC BY-NC 4.0 协议发布。</li>', 1),
    ('<li>All game footage and assets belong to their respective publishers.</li>',
     '<li>所有游戏画面和素材的版权归对应游戏公司所有。</li>', 1),
    # citation and footer
    ('<p class="kicker reveal">Citation</p>', '<p class="kicker reveal">引用</p>', 1),
    ('<h2 class="reveal">Cite the dataset</h2>', '<h2 class="reveal">引用数据集</h2>', 1),
    ('<button class="copy" type="button" id="copy-bib">Copy</button>', '<button class="copy" type="button" id="copy-bib">复制</button>', 1),
    ("""  Counter-Strike&nbsp;2 and Dota&nbsp;2 are trademarks of Valve Corporation; StarCraft&nbsp;II is a trademark of Blizzard Entertainment.
  All other game names and logos are trademarks of their respective owners.
  This project is not affiliated with or endorsed by any of these companies.<br>Contact:""",
     """  Counter-Strike&nbsp;2 和 Dota&nbsp;2 是 Valve 公司的商标，StarCraft&nbsp;II 是暴雪娱乐的商标，其他游戏名称和标志归各自所有者所有。本项目与上述公司无关，也未获其认可。<br>联系方式：""", 1),
    # scripts
    ('aria-label="Full screen"', 'aria-label="全屏"', 1),
    ('<span class="tag left">Real</span><span class="tag right">Generated</span>',
     '<span class="tag left">录像</span><span class="tag right">生成</span>', 1),
    ('`<span><b>${MULTIPLAYER.length}</b>rounds</span>`', '`<span><b>${MULTIPLAYER.length}</b>个回合</span>`', 1),
    ('</b>player views</span>`', '</b>个选手视角</span>`', 1),
    ('</b>maps</span>`', '</b>张地图</span>`', 1),
    ('<b>2&ndash;10</b>players per round</span>', '<b>2&ndash;10</b>人同屏生成</span>', 1),
    ('`${w.views} players · same moment`', '`${w.views} 名选手 · 同一时刻`', 1),
    ('`<span class="count">${w.views} players</span>`', '`<span class="count">${w.views} 人</span>`', 1),
    ('b.textContent = `${size} players`;', 'b.textContent = `${size} 人`;', 1),
    ('labels: ["Player 1 · Zerg", "Player 2 · Protoss"]', 'labels: ["选手 1 · 虫族", "选手 2 · 神族"]', 1),
    ("cap: \"A tournament match on Pylon, Zerg against Protoss: both players' screens during a battle in which 728 units die within 20 seconds.\"",
     'cap: "Pylon 地图锦标赛，虫族对决神族：20 秒内 728 个单位阵亡，双方视角同步呈现。"', 1),
    ('(_, i) => `Hero ${i + 1}`)', '(_, i) => `英雄 ${i + 1}`)', 1),
    ("cap: \"All ten heroes' screens during one team fight, six kills in 20 seconds; each slot's video is mapped to the same replay tick.\"",
     'cap: "一场团战，十位英雄视角同步回放：20 秒内 6 次击杀。"', 1),
    ('(_, i) => `Player ${i + 1}`)', '(_, i) => `选手 ${i + 1}`)', 1),
    ("cap: \"All ten first-person views of one professional round on Nuke, eight kills in 20 seconds; each view is aligned to the round's state ticks.\"",
     'cap: "Nuke 职业比赛的一个回合，十个第一人称视角全员到齐：20 秒内 8 次击杀。"', 1),
    ('event.target.textContent = "Copied";', 'event.target.textContent = "已复制";', 1),
    ('event.target.textContent = "Select & copy";', 'event.target.textContent = "请手动选择复制";', 1),
    ('setTimeout(() => { event.target.textContent = "Copy"; }, 1600);', 'setTimeout(() => { event.target.textContent = "复制"; }, 1600);', 1),
]

missing = []
for en, zh, n in R:
    got = s.count(en)
    if got != n:
        missing.append((got, n, en[:90]))
        continue
    s = s.replace(en, zh)
if missing:
    for got, n, en in missing:
        print(f"count {got} != {n}: {en!r}")
    sys.exit(1)

(site / "index.zh.html").write_text(s, encoding="utf-8")
print("ok", len(R), "replacements")
