# Generated by Django 5.1.2 on 2024-10-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_alter_language_id_alter_snippet_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='slug',
            field=models.CharField(choices=[('abap', 'abap'), ('amdg', 'amdgpu'), ('apl', 'apl'), ('abnf', 'abnf'), ('acti', 'actionscript3'), ('acti', 'actionscript'), ('ada', 'ada'), ('adl', 'adl'), ('agda', 'agda'), ('aheu', 'aheui'), ('allo', 'alloy'), ('ambi', 'ambienttalk'), ('ampl', 'ampl'), ('html', 'html+angular2'), ('angu', 'angular2'), ('antl', 'antlrwithactionscripttarget'), ('antl', 'antlrwithc#target'), ('antl', 'antlrwithcpptarget'), ('antl', 'antlrwithjavatarget'), ('antl', 'antlr'), ('antl', 'antlrwithobjectivectarget'), ('antl', 'antlrwithperltarget'), ('antl', 'antlrwithpythontarget'), ('antl', 'antlrwithrubytarget'), ('apac', 'apacheconf'), ('appl', 'applescript'), ('ardu', 'arduino'), ('arro', 'arrow'), ('artu', 'arturo'), ('asci', 'asciiarmored'), ('asn.', 'asn.1'), ('aspe', 'aspectj'), ('asym', 'asymptote'), ('auge', 'augeas'), ('auto', 'autoit'), ('auto', 'autohotkey'), ('awk', 'awk'), ('bbcb', 'bbcbasic'), ('bbco', 'bbcode'), ('bc', 'bc'), ('bqn', 'bqn'), ('bst', 'bst'), ('bare', 'bare'), ('base', 'basemakefile'), ('bash', 'bash'), ('bash', 'bashsession'), ('batc', 'batchfile'), ('bdd', 'bdd'), ('befu', 'befunge'), ('berr', 'berry'), ('bibt', 'bibtex'), ('blit', 'blitzbasic'), ('blit', 'blitzmax'), ('blue', 'blueprint'), ('bnf', 'bnf'), ('boa', 'boa'), ('boo', 'boo'), ('boog', 'boogie'), ('brai', 'brainfuck'), ('bugs', 'bugs'), ('camk', 'camkes'), ('c', 'c'), ('cmak', 'cmake'), ('c-ob', 'c-objdump'), ('cpsa', 'cpsa'), ('css+', 'css+ul4'), ('aspx', 'aspx-cs'), ('c#', 'c#'), ('ca65', 'ca65assembler'), ('cadl', 'cadl'), ('capd', 'capdl'), ("cap'", "cap'nproto"), ('carb', 'carbon'), ('cbmb', 'cbmbasicv2'), ('cddl', 'cddl'), ('ceyl', 'ceylon'), ('cfen', 'cfengine3'), ('chai', 'chaiscript'), ('chap', 'chapel'), ('char', 'charmci'), ('html', 'html+cheetah'), ('java', 'javascript+cheetah'), ('chee', 'cheetah'), ('xml+', 'xml+cheetah'), ('cirr', 'cirru'), ('clay', 'clay'), ('clea', 'clean'), ('cloj', 'clojure'), ('cloj', 'clojurescript'), ('cobo', 'cobolfree'), ('cobo', 'cobol'), ('coff', 'coffeescript'), ('cold', 'coldfusioncfc'), ('cold', 'coldfusionhtml'), ('cfst', 'cfstatement'), ('coma', 'comal-80'), ('comm', 'commonlisp'), ('comp', 'componentpascal'), ('coq', 'coq'), ('cpli', 'cplint'), ('c++', 'c++'), ('cpp-', 'cpp-objdump'), ('crms', 'crmsh'), ('croc', 'croc'), ('cryp', 'cryptol'), ('crys', 'crystal'), ('csou', 'csounddocument'), ('csou', 'csoundorchestra'), ('csou', 'csoundscore'), ('css+', 'css+django/jinja'), ('css+', 'css+ruby'), ('css+', 'css+genshitext'), ('css', 'css'), ('css+', 'css+php'), ('css+', 'css+smarty'), ('cuda', 'cuda'), ('cyph', 'cypher'), ('cyth', 'cython'), ('d', 'd'), ('d-ob', 'd-objdump'), ('darc', 'darcspatch'), ('dart', 'dart'), ('dasm', 'dasm16'), ('dax', 'dax'), ('debi', 'debiancontrolfile'), ('delp', 'delphi'), ('desk', 'desktopfile'), ('devi', 'devicetree'), ('dg', 'dg'), ('diff', 'diff'), ('djan', 'django/jinja'), ('zone', 'zone'), ('dock', 'docker'), ('dtd', 'dtd'), ('duel', 'duel'), ('dyla', 'dylansession'), ('dyla', 'dylan'), ('dyla', 'dylanlid'), ('ecl', 'ecl'), ('ec', 'ec'), ('earl', 'earlgrey'), ('easy', 'easytrieve'), ('ebnf', 'ebnf'), ('eiff', 'eiffel'), ('elix', 'elixiriexsession'), ('elix', 'elixir'), ('elm', 'elm'), ('elpi', 'elpi'), ('emac', 'emacslisp'), ('e-ma', 'e-mail'), ('erb', 'erb'), ('erla', 'erlang'), ('erla', 'erlangerlsession'), ('html', 'html+evoque'), ('evoq', 'evoque'), ('xml+', 'xml+evoque'), ('exec', 'execline'), ('ezhi', 'ezhil'), ('f#', 'f#'), ('fsta', 'fstar'), ('fact', 'factor'), ('fanc', 'fancy'), ('fant', 'fantom'), ('feli', 'felix'), ('fenn', 'fennel'), ('fift', 'fift'), ('fish', 'fish'), ('flat', 'flatline'), ('flos', 'floscript'), ('fort', 'forth'), ('fort', 'fortranfixed'), ('fort', 'fortran'), ('foxp', 'foxpro'), ('free', 'freefem'), ('func', 'func'), ('futh', 'futhark'), ('gaps', 'gapsession'), ('gap', 'gap'), ('gdsc', 'gdscript'), ('glsl', 'glsl'), ('gsql', 'gsql'), ('gas', 'gas'), ('g-co', 'g-code'), ('gens', 'genshi'), ('gens', 'genshitext'), ('gett', 'gettextcatalog'), ('gher', 'gherkin'), ('gnup', 'gnuplot'), ('go', 'go'), ('golo', 'golo'), ('good', 'gooddata-cl'), ('gosu', 'gosu'), ('gosu', 'gosutemplate'), ('grap', 'graphql'), ('grap', 'graphviz'), ('grof', 'groff'), ('groo', 'groovy'), ('hlsl', 'hlsl'), ('html', 'html+ul4'), ('haml', 'haml'), ('html', 'html+handlebars'), ('hand', 'handlebars'), ('hask', 'haskell'), ('haxe', 'haxe'), ('hexd', 'hexdump'), ('hsai', 'hsail'), ('hspe', 'hspec'), ('html', 'html+django/jinja'), ('html', 'html+genshi'), ('html', 'html'), ('html', 'html+php'), ('html', 'html+smarty'), ('http', 'http'), ('hxml', 'hxml'), ('hy', 'hy'), ('hybr', 'hybris'), ('idl', 'idl'), ('icon', 'icon'), ('idri', 'idris'), ('igor', 'igor'), ('info', 'inform6'), ('info', 'inform6template'), ('info', 'inform7'), ('ini', 'ini'), ('io', 'io'), ('ioke', 'ioke'), ('ircl', 'irclogs'), ('isab', 'isabelle'), ('j', 'j'), ('jmes', 'jmespath'), ('jslt', 'jslt'), ('jags', 'jags'), ('jane', 'janet'), ('jasm', 'jasmin'), ('java', 'java'), ('java', 'javascript+django/jinja'), ('java', 'javascript+ruby'), ('java', 'javascript+genshitext'), ('java', 'javascript'), ('java', 'javascript+php'), ('java', 'javascript+smarty'), ('java', 'javascript+ul4'), ('jcl', 'jcl'), ('jsgf', 'jsgf'), ('json', 'jsonbareobject'), ('json', 'json-ld'), ('json', 'json'), ('json', 'jsonnet'), ('java', 'javaserverpage'), ('jsx', 'jsx'), ('juli', 'juliaconsole'), ('juli', 'julia'), ('jutt', 'juttle'), ('k', 'k'), ('kal', 'kal'), ('kcon', 'kconfig'), ('kern', 'kernellog'), ('koka', 'koka'), ('kotl', 'kotlin'), ('kuin', 'kuin'), ('kust', 'kusto'), ('lsl', 'lsl'), ('css+', 'css+lasso'), ('html', 'html+lasso'), ('java', 'javascript+lasso'), ('lass', 'lasso'), ('xml+', 'xml+lasso'), ('ldap', 'ldapconfigurationfile'), ('ldif', 'ldif'), ('lean', 'lean'), ('lean', 'lean4'), ('less', 'lesscss'), ('ligh', 'lighttpdconfigurationfile'), ('lily', 'lilypond'), ('limb', 'limbo'), ('liqu', 'liquid'), ('lite', 'literateagda'), ('lite', 'literatecryptol'), ('lite', 'literatehaskell'), ('lite', 'literateidris'), ('live', 'livescript'), ('llvm', 'llvm'), ('llvm', 'llvm-mirbody'), ('llvm', 'llvm-mir'), ('logo', 'logos'), ('logt', 'logtalk'), ('lua', 'lua'), ('luau', 'luau'), ('mcfu', 'mcfunction'), ('mcsc', 'mcschema'), ('mime', 'mime'), ('mips', 'mips'), ('mooc', 'moocode'), ('msdo', 'msdossession'), ('maca', 'macaulay2'), ('make', 'makefile'), ('css+', 'css+mako'), ('html', 'html+mako'), ('java', 'javascript+mako'), ('mako', 'mako'), ('xml+', 'xml+mako'), ('maql', 'maql'), ('mark', 'markdown'), ('mask', 'mask'), ('maso', 'mason'), ('math', 'mathematica'), ('matl', 'matlab'), ('matl', 'matlabsession'), ('maxi', 'maxima'), ('meso', 'meson'), ('mini', 'minid'), ('mini', 'miniscript'), ('mode', 'modelica'), ('modu', 'modula-2'), ('moin', 'moinmoin/tracwikimarkup'), ('mojo', 'mojo'), ('monk', 'monkey'), ('mont', 'monte'), ('moon', 'moonscript'), ('mose', 'mosel'), ('css+', 'css+mozpreproc'), ('mozh', 'mozhashpreproc'), ('java', 'javascript+mozpreproc'), ('mozp', 'mozpercentpreproc'), ('xul+', 'xul+mozpreproc'), ('mql', 'mql'), ('mscg', 'mscgen'), ('mupa', 'mupad'), ('mxml', 'mxml'), ('mysq', 'mysql'), ('css+', 'css+myghty'), ('html', 'html+myghty'), ('java', 'javascript+myghty'), ('mygh', 'myghty'), ('xml+', 'xml+myghty'), ('ncl', 'ncl'), ('nsis', 'nsis'), ('nasm', 'nasm'), ('objd', 'objdump-nasm'), ('neme', 'nemerle'), ('nesc', 'nesc'), ('nest', 'nestedtext'), ('newl', 'newlisp'), ('news', 'newspeak'), ('ngin', 'nginxconfigurationfile'), ('nimr', 'nimrod'), ('nit', 'nit'), ('nix', 'nix'), ('node', 'node.jsreplconsolesession'), ('notm', 'notmuch'), ('nusm', 'nusmv'), ('nump', 'numpy'), ('objd', 'objdump'), ('obje', 'objective-c'), ('obje', 'objective-c++'), ('obje', 'objective-j'), ('ocam', 'ocaml'), ('octa', 'octave'), ('odin', 'odin'), ('omgi', 'omginterfacedefinitionlanguage'), ('ooc', 'ooc'), ('opa', 'opa'), ('open', 'openedgeabl'), ('open', 'openscad'), ('orgm', 'orgmode'), ('text', 'textoutput'), ('pacm', 'pacmanconf'), ('pan', 'pan'), ('para', 'parasail'), ('pawn', 'pawn'), ('peg', 'peg'), ('perl', 'perl6'), ('perl', 'perl'), ('phix', 'phix'), ('php', 'php'), ('pig', 'pig'), ('pike', 'pike'), ('pkgc', 'pkgconfig'), ('pl/p', 'pl/pgsql'), ('poin', 'pointless'), ('pony', 'pony'), ('port', 'portugol'), ('post', 'postscript'), ('post', 'postgresqlconsole(psql)'), ('post', 'postgresqlexplaindialect'), ('post', 'postgresqlsqldialect'), ('povr', 'povray'), ('powe', 'powershell'), ('powe', 'powershellsession'), ('praa', 'praat'), ('proc', 'procfile'), ('prol', 'prolog'), ('prom', 'promql'), ('prom', 'promela'), ('prop', 'properties'), ('prot', 'protocolbuffer'), ('prql', 'prql'), ('psys', 'psyshconsolesessionforphp'), ('ptx', 'ptx'), ('pug', 'pug'), ('pupp', 'puppet'), ('pypy', 'pypylog'), ('pyth', 'python2.x'), ('pyth', 'python2.xtraceback'), ('pyth', 'pythonconsolesession'), ('pyth', 'python'), ('pyth', 'pythontraceback'), ('pyth', 'python+ul4'), ('qbas', 'qbasic'), ('q', 'q'), ('qvto', 'qvto'), ('qlik', 'qlik'), ('qml', 'qml'), ('rcon', 'rconsole'), ('rela', 'relax-ngcompact'), ('rpms', 'rpmspec'), ('rack', 'racket'), ('rage', 'ragelinchost'), ('rage', 'ragelincpphost'), ('rage', 'ragelindhost'), ('embe', 'embeddedragel'), ('rage', 'ragelinjavahost'), ('rage', 'ragel'), ('rage', 'ragelinobjectivechost'), ('rage', 'ragelinrubyhost'), ('rawt', 'rawtokendata'), ('rd', 'rd'), ('reas', 'reasonml'), ('rebo', 'rebol'), ('red', 'red'), ('redc', 'redcode'), ('reg', 'reg'), ('reso', 'resourcebundle'), ('rexx', 'rexx'), ('rhtm', 'rhtml'), ('ride', 'ride'), ('rita', 'rita'), ('robo', 'roboconfgraph'), ('robo', 'roboconfinstances'), ('robo', 'robotframework'), ('rql', 'rql'), ('rsl', 'rsl'), ('rest', 'restructuredtext'), ('traf', 'trafficscript'), ('ruby', 'rubyirbsession'), ('ruby', 'ruby'), ('rust', 'rust'), ('sas', 'sas'), ('s', 's'), ('stan', 'standardml'), ('snbt', 'snbt'), ('sarl', 'sarl'), ('sass', 'sass'), ('savi', 'savi'), ('scal', 'scala'), ('scam', 'scaml'), ('scdo', 'scdoc'), ('sche', 'scheme'), ('scil', 'scilab'), ('scss', 'scss'), ('sed', 'sed'), ('shex', 'shexc'), ('shen', 'shen'), ('siev', 'sieve'), ('silv', 'silver'), ('sing', 'singularity'), ('slas', 'slash'), ('slim', 'slim'), ('slur', 'slurm'), ('smal', 'smali'), ('smal', 'smalltalk'), ('smar', 'smartgameformat'), ('smar', 'smarty'), ('smit', 'smithy'), ('snob', 'snobol'), ('snow', 'snowball'), ('soli', 'solidity'), ('soon', 'soong'), ('soph', 'sophia'), ('sour', 'sourcepawn'), ('debi', 'debiansourcelist'), ('spar', 'sparql'), ('spic', 'spice'), ('sql+', 'sql+jinja'), ('sql', 'sql'), ('sqli', 'sqlite3con'), ('squi', 'squidconf'), ('srci', 'srcinfo'), ('scal', 'scalateserverpage'), ('stan', 'stan'), ('stat', 'stata'), ('supe', 'supercollider'), ('swif', 'swift'), ('swig', 'swig'), ('syst', 'systemverilog'), ('syst', 'systemd'), ('tap', 'tap'), ('typo', 'typographicnumbertheory'), ('toml', 'toml'), ('tact', 'tact'), ('tads', 'tads3'), ('tal', 'tal'), ('tasm', 'tasm'), ('tcl', 'tcl'), ('tcsh', 'tcsh'), ('tcsh', 'tcshsession'), ('tea', 'tea'), ('teal', 'teal'), ('tera', 'teratermmacro'), ('term', 'termcap'), ('term', 'terminfo'), ('terr', 'terraform'), ('tex', 'tex'), ('text', 'textonly'), ('thin', 'thingsdb'), ('thri', 'thrift'), ('tidd', 'tiddler'), ('tl-b', 'tl-b'), ('tlsp', 'tlspresentationlanguage'), ('todo', 'todotxt'), ('tran', 'transact-sql'), ('tree', 'treetop'), ('turt', 'turtle'), ('html', 'html+twig'), ('twig', 'twig'), ('type', 'typescript'), ('typo', 'typoscriptcssdata'), ('typo', 'typoscripthtmldata'), ('typo', 'typoscript'), ('typs', 'typst'), ('ul4', 'ul4'), ('ucod', 'ucode'), ('unic', 'unicon'), ('unix', 'unix/linuxconfigfiles'), ('urbi', 'urbiscript'), ('urle', 'urlencoded'), ('usd', 'usd'), ('vbsc', 'vbscript'), ('vcl', 'vcl'), ('vcls', 'vclsnippets'), ('vctr', 'vctreestatus'), ('vgl', 'vgl'), ('vala', 'vala'), ('aspx', 'aspx-vb'), ('vb.n', 'vb.net'), ('html', 'html+velocity'), ('velo', 'velocity'), ('xml+', 'xml+velocity'), ('veri', 'verifpal'), ('veri', 'verilog'), ('vhdl', 'vhdl'), ('viml', 'viml'), ('visu', 'visualprologgrammar'), ('visu', 'visualprolog'), ('vype', 'vyper'), ('wdif', 'wdiff'), ('weba', 'webassembly'), ('webi', 'webidl'), ('webg', 'webgpushadinglanguage'), ('whil', 'whiley'), ('wiki', 'wikitext'), ('worl', 'worldofwarcrafttoc'), ('wren', 'wren'), ('x10', 'x10'), ('xml+', 'xml+ul4'), ('xque', 'xquery'), ('xml+', 'xml+django/jinja'), ('xml+', 'xml+ruby'), ('xml', 'xml'), ('xml+', 'xml+php'), ('xml+', 'xml+smarty'), ('xorg', 'xorg'), ('x++', 'x++'), ('xslt', 'xslt'), ('xten', 'xtend'), ('xtla', 'xtlang'), ('yaml', 'yaml+jinja'), ('yaml', 'yaml'), ('yang', 'yang'), ('yara', 'yara'), ('zeek', 'zeek'), ('zeph', 'zephir'), ('zig', 'zig'), ('ansy', 'ansysparametricdesignlanguage')], max_length=50),
        ),
    ]
