#ENNEAGRAM

import pandas as pd
import numpy as np
import streamlit as st
import joblib


st.set_page_config(layout='wide')

st.header(":red[ENNEAGRAM]", divider='rainbow')

tab_1, tab_2, tab_3 = st.tabs(['Enneagram nedir?', 'Test', 'Kişılık Türleri'])

tab_1.image("enneagram.jpg",  width=220)

col_1, col_2 = tab_1.columns(2, gap='large')

col_1.subheader('Enneagram Nedir:question:', divider='rainbow')

col_1.markdown('Bir bakış açısından, Enneagram, Enneagramdaki her sayı bir türü ifade eden dokuz farklı kişilik tipinden oluşan bir set olarak görülebilir. Dokuz türün hepsinde kendinizden biraz bulmak yaygındır, ancak bunlardan biri kendinize en yakın olarak öne çıkmalıdır. Bu sizin temel kişilik tipinizdir. Herkes, doğuştan gelen mizaç ve diğer doğum öncesi faktörlerin türümüzün ana belirleyicileri olduğu, kişiliğine hakim olan dokuz tipten biriyle çocukluktan çıkar. Bu, büyük Enneagram yazarlarının çoğunun hemfikir olduğu bir alandır - baskın bir türle doğarız. Akabinde, bu doğuştan gelen yönelim, erken çocukluk ortamımıza uyum sağlamayı öğrenme yollarımızı büyük ölçüde belirler. Aynı zamanda ebeveyn figürlerimize karşı belirli bilinçsiz yönelimlere yol açıyor gibi görünüyor, ancak bunun neden böyle olduğunu hala bilmiyoruz. Her halükarda, çocuklar dört veya beş yaşına geldiklerinde, bilinçleri ayrı bir benlik duygusuna sahip olmak için yeterince gelişmiştir. Kimlikleri hala çok akıcı olsa da, bu yaşta çocuklar kendilerini kurmaya ve dünyaya kendi başlarına uymanın yollarını bulmaya başlarlar.Bu nedenle, kişiliğimizin genel yönelimi, gelişimini etkileyen tüm çocukluk faktörlerinin (genetik dahil) bütünlüğünü yansıtır.')

col_2.subheader('Temel Kişilik Tipiniz',divider='rainbow')

col_2.markdown('**1**. İnsanlar bir temel kişilik tipinden diğerine değişmez.')

col_2.markdown('2. Kişilik tiplerinin tanımları evrenseldir ve hiçbir tip doğası gereği erkeksi veya kadınsı olmadığı için erkekler ve kadınlar için eşit olarak geçerlidir.')

col_2.markdown('3. Temel tipinizin tanımındaki her şey sizin için her zaman geçerli olmayacaktır, çünkü kişilik tipinizi oluşturan sağlıklı, ortalama ve sağlıksız özellikler arasında sürekli dalgalanırsınız.')

col_2.markdown('4. Enneagram, türlerin her birini belirtmek için sayıları kullanır, çünkü sayılar nötr değerdir - olumlu veya olumsuz bir şey belirtmeden her türün tüm tutum ve davranışlarını ima eder. Psikiyatride kullanılan etiketlerin aksine, sayılar aşağılayıcı olmadan bir kişi hakkında çok şey göstermenin tarafsız, kısaltma bir yolunu sağlar.')

col_2.markdown('5. Türlerin sayisal sıralaması anlamlı değildir. Daha büyük bir sayı, daha küçük bir sayıdan daha iyi değildir; Dokuz olmak İkiden daha iyi değildir çünkü dokuz daha büyük bir sayıdır.')

col_2.markdown('6. Hiçbir tür doğal olarak diğerlerinden daha iyi veya daha kötü değildir. Tüm kişilik tipleri benzersiz varlıklara ve yükümlülüklere sahip olsa da, bazı türlerin herhangi bir kültür veya grupta diğerlerinden daha arzu edilir olduğu düşünülebilir. Ayrıca, şu ya da bu nedenle, belirli bir tip olmaktan mutlu olmayabilirsiniz. Bununla birlikte, tüm türler hakkında daha fazla bilgi edindikçe, her birinin benzersiz varlıkları olduğu gibi, her birinin benzersiz yükümlülükleri olduğunu göreceksiniz. İdeal olan, başka bir türdeki varlıkları taklit etmek değil, en iyi benliğiniz olmaktır.')

tab_1.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)

tip_1 = [0]
tip_2 = [0]
tip_3 = [0]
tip_4 = [0]
tip_5 = [0]
tip_6 = [0]
tip_7 = [0]
tip_8 = [0]
tip_9 = [0]


tab_2.title('Enneagram Testi')

tab_2.subheader('Aşağıdaki ifadelerin kendiniz için uygun olduğunu düşünüyorsanız "Evet" değilse "Hayır" cevabını seçiniz.')

st.markdown("""<style>div[class*="stRadio"] > label > div[data-testid="stMarkdownContainer"] > p {font-size: 24px;} </style>""", unsafe_allow_html = True)

answers = ['Evet', 'Hayır']

question_1 = tab_2.radio('1.Daha çok asil ruhlu ve yüce gönüllü bir idealistim.', answers)

if question_1 == 'Evet':
    tip_1.append(1)
else:
    tip_1.append(0)

question_2 = tab_2.radio('2.İnsanlarla arama mesafe koymayı tercih ederim.', answers)

if question_2 == 'Evet':
    tip_5.append(1)
else:
    tip_5.append(0)

question_3 = tab_2.radio('3.Yüzleşmeden veya çatışma yaşamaktan kaçınırım.', answers)

if question_3 == 'Evet':
    tip_9.append(1)
else:
    tip_9.append(0)

question_4 = tab_2.radio('4.Misafirperver bir insanım ve hayatıma yeni arkadaşların girmesinden hoşlanırım.', answers)

if question_4 == 'Evet':
    tip_2.append(1)
else:
    tip_2.append(0)

question_5 = tab_2.radio('5.Başkaları gücüme ve kararlılığıma güvenirler ve dayanırlar.', answers)

if question_5 == 'Evet':
    tip_8.append(1)
else:
    tip_8.append(0)

question_6 = tab_2.radio('6.Genellikle bir işi yapmak için duygularımı bir kenara bırakabilirim.', answers)

if question_6 == 'Evet':
    tip_3.append(1)
else:
    tip_3.append(0)

question_7 = tab_2.radio('7.Benim için rahatlamak zordur ve potansiyel problemlere karşı endişelenmeden duramam.', answers)

if question_7 == 'Evet':
    tip_6.append(1)
else:
    tip_6.append(0)

question_8 = tab_2.radio('8.Kendimle ilgili açıkça konuşamam ve kendimi çok iyi ifade edemem.', answers)

if question_8 == 'Evet':
    tip_4.append(1)
else:
    tip_4.append(0)

question_9 = tab_2.radio('9.Fevri, bireysel ve içinden geldiği gibi davranmaya meyilliyim ve eğlence severim.', answers)

if question_9 == 'Evet':
    tip_7.append(1)
else:
    tip_7.append(0)

question_10 = tab_2.radio('10.Genellikle maceracıyım ve risk alırım.', answers)

if question_10 == 'Evet':
    tip_7.append(1)
else:
    tip_7.append(0)

question_11 = tab_2.radio('11.Öfke, mükemmellik ve sabırsızlıktan dolayı sık sık sorun yaşarım.', answers)

if question_11 == 'Evet':
    tip_1.append(1)
else:
    tip_1.append(0)

question_12 = tab_2.radio('12.Cesur, baskın ve otoriter olmaya eğilimliyım.', answers)

if question_12 == 'Evet':
    tip_8.append(1)
else:
    tip_8.append(0)

question_13 = tab_2.radio('13.Sıkıntılı olduğumda problemlerimi kara kara düşünürüm.', answers)

if question_13 == 'Evet':
    tip_4.append(1)
else:
    tip_4.append(0)

question_14 = tab_2.radio('14.İnsanlara sevgi ve merhamet gösterme ihtiyacı hissederim.', answers)

if question_14 == 'Evet':
    tip_2.append(1)
else:
    tip_2.append(0)

question_15 = tab_2.radio('15.Dalgın, uzak duran veya ilgisiz olma eğilimindeyim.', answers)

if question_15 == 'Evet':
    tip_5.append(1)
else:
    tip_5.append(0)

question_16 = tab_2.radio('16.Müdahil veya girişken olma isteksizliğim insanlarla sorun yaşamama neden olur.', answers)

if question_16 == 'Evet':
    tip_9.append(1)
else:
    tip_9.append(0)

question_17 = tab_2.radio('17.Yüksek motivasyonlu ve tuttuğunu koparan bir girişimciyim.', answers)

if question_17 == 'Evet':
    tip_3.append(1)
else:
    tip_3.append(0)

question_18 = tab_2.radio('18.Kendime karşı güvensiz kalırım ve tereddütlü ve dikkatli olmaya eğilimliyim.', answers)

if question_18 == 'Evet':
    tip_6.append(1)
else:
    tip_6.append(0)

question_19 = tab_2.radio('19.Biraz duygusal ve hassas birisiyim.', answers)

if question_19 == 'Evet':
    tip_2.append(1)
else:
    tip_2.append(0)

question_20 = tab_2.radio('20.Tipik olarak istikrar ve iç huzurumu korumaya istekliyim.', answers)

if question_20 == 'Evet':
    tip_9.append(1)
else:
    tip_9.append(0)

question_21 = tab_2.radio('21.Spontane biriyim ve problemlere karşı doğaçlama yapmayı tercih ederim.', answers)

if question_21 == 'Evet':
    tip_7.append(1)
else:
    tip_7.append(0)

question_22 = tab_2.radio('22.Harekete geçmem çok zamanımı alır.', answers)

if question_22 == 'Evet':
    tip_1.append(1)
else:
    tip_1.append(0)

question_23 = tab_2.radio('23.Sürekli geçmişteki şeyleri düşünüp durma eğilimindeyim.', answers)

if question_23 == 'Evet':
    tip_4.append(1)
else:
    tip_4.append(0)

question_24 = tab_2.radio('24.Ödül ve kişisel tanınırlık potansiyeli taşıyan aktivitelerin peşinden giderim.', answers)

if question_24 == 'Evet':
    tip_3.append(1)
else:
    tip_3.append(0)

question_25 = tab_2.radio('25.Birçok durumda başkasına liderlik etmeyi tercih ederim.', answers)

if question_25 == 'Evet':
    tip_8.append(1)
else:
    tip_8.append(0)

question_26 = tab_2.radio('26.Başkaları benim feraset, anlayış ve bilgime güvenirler.', answers)

if question_26 == 'Evet':
    tip_5.append(1)
else:
    tip_5.append(0)

question_27 = tab_2.radio('27.Güvenilir ve adanmış olmaktan gurur duyarım.', answers)

if question_27 == 'Evet':
    tip_6.append(1)
else:
    tip_6.append(0)

question_28 = tab_2.radio('28.Genellikle kuvvetli fikirlerim  ve birşeylerin nasıl olması gerektiğine dair hislerim var.', answers)

if question_28 == 'Evet':
    tip_1.append(1)
else:
    tip_1.append(0)

question_29 = tab_2.radio('29.İnsanlarla yaşadığım zorlukların çoğu alınganlığım ve herşeyi kişisel algılamamdan kaynaklanmaktadır.', answers)

if question_29 == 'Evet':
    tip_4.append(1)
else:
    tip_4.append(0)

question_30 = tab_2.radio('30.Başkalarının aktivitelerinin dışında kalacağımdan endişelenirim.', answers)

if question_30 == 'Evet':
    tip_2.append(1)
else:
    tip_2.append(0)

question_31 = tab_2.radio('31.Başkalarıyla uyumlu olmayı isterim. Çok fazla sivrilmekten göze batmaktan rahatsızlik duyarım.', answers)

if question_31 == 'Evet':
    tip_9.append(1)
else:
    tip_9.append(0)

question_32 = tab_2.radio('32.Genellikle sosyal sorumluluklarımı çok ciddiye alırım.', answers)

if question_32 == 'Evet':
    tip_6.append(1)
else:
    tip_6.append(0)

question_33 = tab_2.radio('33.Başkalarında bakımlı ve imrenilen birisi izlenimi bıraktığımı farkettim.', answers)

if question_33 == 'Evet':
    tip_3.append(1)
else:
    tip_3.append(0)

question_34 = tab_2.radio('34.Yeni şeylere açık olma ve onlardan zevk alma konusunda kendimle gurur duyarım.', answers)

if question_34 == 'Evet':
    tip_7.append(1)
else:
    tip_7.append(0)

question_35 = tab_2.radio('35.Kendi küçük dünyamda yaşamayı tercih ederim.', answers)

if question_35 == 'Evet':
    tip_5.append(1)
else:
    tip_5.append(0)

question_36 = tab_2.radio('36.Benim olumlu özeliklerimden biri de durumları kontrol altında tutma becerimdir.', answers)

if question_36 == 'Evet':
    tip_8.append(1)
else:
    tip_8.append(0)

tab_2.write('')


sum_lists = [sum(tip_1), sum(tip_2), sum(tip_3), sum(tip_4), sum(tip_5), sum(tip_6), sum(tip_7), sum(tip_8), sum(tip_9)]

max_list_index = sum_lists.index(max(sum_lists))

sonuc = tab_2.button('Sonuç')

if sonuc:
    tab_2.write(f"Kişilik tipin tip{max_list_index + 1}")


tab_2.markdown('Kişilik tipinizle ilgili daha fazla bilgi almak için :red[Kişilik Türleri] bölümünü inceleyebilirsiniz.')


type_1, type_2, type_3, type_4, type_5, type_6, type_7, type_8, type_9 = tab_3.tabs(['Tip 1', 'Tip 2', 'Tip 3', 'Tip 4', 'Tip 5', 'Tip 6', 'Tip 7', 'Tip 8', 'Tip 9'])

type_1.header(":red[Mükemmeliyetçi]", divider='rainbow')


type_1.image("type1.gif",  width=260)

type_1.subheader('Rasyonel, İdealist Tip: İlkeli, Amaçlı, Kendi Kendini Kontrol Eden ve Mükemmeliyetçi')

tp1_col1, tp1_col2 = type_1.columns(2, gap='large')

tp1_col1.write('')

tp1_col1.subheader('Reformcu')

tp1_col1.markdown('Kişi vicdanlı ve etiktir, güçlü bir doğru ve yanlış duygusuna sahiptir. Onlar öğretmenler, haçlılar ve değişimin savunucularıdır: her zaman bir şeyleri geliştirmek için çabalarlar, ancak hata yapmaktan korkarlar. İyi organize edilmiş, düzenli ve titiz, yüksek standartları korumaya çalışırlar, ancak kritik ve mükemmeliyetçi olabilirler. Genellikle kızgınlık ve sabırsızlıkla ilgili sorunları vardır. En iyileri: bilge, anlayışlı, gerçekçi ve asil. Ahlaki olarak kahramanca olabilir.')

tp1_col1.markdown(':red[*Temel Korku]: Yozlaşmış/kötü, kusurlu olmak')

tp1_col1.markdown(':red[*Temel Arzu]: İyi olmak, bütünlüğe sahip olmak, dengeli olmak')

tp1_col1.markdown(':red[*Anahtar Motivasyonlar]: Haklı olmak, daha yükseğe çabalamak ve her şeyi geliştirmek, idealleriyle tutarlı olmak, kendilerini haklı çıkarmak, kimse tarafından kınanmamak için eleştirinin ötesinde olmak ister.')

tp1_col1.markdown(':red[Örnekler:] Konfüçyüs, Platon, Salahuddin Ayyubi, Joan of Arc, Sir Thomas More, Mahatma Gandhi, Papa John Paul II, Nelson Mandela, Margaret Thatcher, Prens Charles, Kate Middleton Cambridge Düşesi, Jimmy Carter, Michelle Obama, Al Gore, Hillary Clinton, Rudy Giuliani, Elliot Spitzer, Osama bin Laden, George Bernard Shaw, Anita Roddick (The Body Shop), Martha Stewart, Celine Dion, Ralph Nader, Noam Chomsky, Jane Fonda, Meryl Streep, Harrison Ford, Helen Hunt, Captain “Sully” Sullenberger”')

tp1_col2.subheader('Tip Bir—Gelişim Düzeyleri')

tp1_col2.markdown('Sağlıklı Seviyeler')

tp1_col2.markdown(':red[Seviye 1 (En İyisi)]: Olağanüstü bilge ve anlayışlı olun. Ne olduğunu kabul ederek, her an atılacak en iyi eylemi bilerek, aşkın bir şekilde gerçekçi hale gelirler. İnsancıl, ilham verici ve umutlu: gerçek duyulacak.')

tp1_col2.markdown(':red[Seviye 2]: Güçlü kişisel inançları olan vicdanlı: yoğun bir doğru ve yanlış duygusuna, kişisel dini ve ahlaki değerlere sahiptirler. Akılcı, makul, öz disiplinli, olgun, her şeyde ılımlı olmak dileğiyle.')

tp1_col2.markdown(':red[Seviye 3]: Son derece ilkeli, her zaman adil, objektif ve etik olmak ister: hakikat ve adalet birincil değerler. Sorumluluk duygusu, kişisel bütünlük ve daha yüksek bir amaca sahip olmak genellikle onları gerçeğin öğretmen ve tanıkları yapar.')

tp1_col2.markdown('Ortalama Seviyeler')

tp1_col2.markdown(':red[Seviye 4]: Gerçeklikten memnun değiller, her şeyi iyileştirmenin kendilerine bağlı olduğunu hissederek yüksek fikirli idealistler olurlar: haçlılar, savunucular, eleştirmenler. "Nedenler"e ve başkalarına işlerin nasıl "olması gerektiğini" açıklamak.')

tp1_col2.markdown(':red[Seviye 5]: Hata yapmaktan korkmak: her şey idealleriyle tutarlı olmalıdır. Düzenli ve iyi organize olun, ancak kişisel olmayan, püriten, duygusal olarak dar, duygularını ve dürtülerini katı bir şekilde kontrol altında tutar. Genellikle işkolikler—"anal-kompulsif," dakik, bilgiç ve titiz.')

tp1_col2.markdown(':red[Seviye 6]: Hem benlik hem de diğerleri için son derece eleştirel: seçici, yargılayıcı, mükemmeliyetçi. Her şey hakkında çok fikirli: insanları düzeltmek ve onları "doğru şeyi yapmaları" için rozetlemek - gördükleri gibi. Sabırsız, reçetelerine göre yapılmadığı sürece hiçbir şeyden asla memnun değil. Ahlaki, azarlayıcı, aşındırıcı ve öfkeyle öfkeli.')

tp1_col2.markdown('Sağlıksız Seviyeler')

tp1_col2.markdown(':red[Seviye 7]: Son derece dogmatik, kendini beğenmiş, hoşgörüsüz ve esnek olmayabilir. Mutlaklarla uğraşmaya başlayın: "Gerçeği" sadece onlar bilir. Diğer herkes yanılıyor: kendi eylemlerini rasyonalize ederken yargılarda çok şiddetli.')

tp1_col2.markdown(':red[Seviye 8]: Kusurluluk ve başkalarının yanlış davranışları konusunda takıntılı olun, ancak çelişkili eylemlere düşseler de, ikiyüzlü bir şekilde vaaz ettiklerinin tam tersini yapın.')

tp1_col2.markdown(':red[Seviye 9]: Başkalarına karşı kınayıcı olun, kendilerini zalimlerden kurtarmak için cezalandırıcı ve acımasız olun. Şiddetli depresyonlar, sinir krizleri ve intihar girişimleri muhtemeldir. Genellikle Obsesif-Kompulsif ve Depresif kişilik bozukluklarına karşılık gelir.')

tp1_col1.write('')

tp1_col1.markdown(':red[Bağımlılıklar]')

tp1_col1.markdown('Diyetlerin, vitaminlerin ve temizleme tekniklerinin (oruç, diyet hapları, lavman) aşırı kullanımı. Self-control için az yemek: aşırı durumlarda anoreksi ve bulimia. Gerginliği azaltmak için alkol.')

tp1_col1.markdown(':red[Kişisel Gelişim Önerileri]')

tp1_col1.markdown('*Rahatlamayı öğren. Her şeyin size kalmış olduğunu veya başaramadığınız şeyin kaos ve felaketle sonuçlanacağını hissetmeden kendinize biraz zaman ayırın. Neyse ki, dünyanın kurtuluşu, bazen öyle olduğunu hissetseniz de, yalnızca size bağlı değildir')

tp1_col1.markdown('*Başkalarına öğretecek çok şeyiniz var ve muhtemelen iyi bir öğretmensiniz, ancak başkalarının hemen değişmesini beklemeyin.')

tp1_col1.markdown('Geri adım atmaya çalışın ve öfkenizin insanları yabancılaştırdığını, böylece söylemeniz gereken iyi şeylerin çoğunu duyamayacaklarını görün.')


type_1.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)

type_2.header(':red[Yardımsever]', divider='rainbow')

type_2.image('type2.gif', width=260)

type_2.subheader('Şefkatli, Kişilerarası Tip: Cömert, Gösterici, İnsanları Memnun Eden ve Sahiplenici')

tp2_col1, tp2_col2 = type_2.columns(2, gap='large')

tp2_col1.write('')

tp2_col1.subheader('Yardımsever')

tp2_col1.markdown('Empatik, samimi ve sıcak kalpli. Arkadaş canlısı, cömert ve fedakardırlar, ancak aynı zamanda duygusal, gurur verici ve insanları memnun edebilirler. İyi-nanlıdırlar ve başkalarına yakın olmaya yönlendirilirler, ancak ihtiyaç duyulması için başkaları için bir şeyler yapmaya kayabilirler. Genellikle sahiplenme ve kendi ihtiyaçlarını kabul etme ile ilgili sorunları vardır. En iyi halleriyle: bencil olmayan ve özgecil, başkalarına karşı koşulsuz sevgileri vardır')

tp2_col1.markdown(':red[*Temel Korku]: İstenmeyen olmak, sevilmeye layık olmamak')

tp2_col1.markdown(':red[*Temel Arzu]: Sevildiğini hissetmek')

tp2_col1.markdown(':red[*Anahtar Motivasyonlar]: Sevilmek, başkalarına karşı duygularını ifade etmek, ihtiyaç duyulmak ve takdir edilmek, başkalarının onlara cevap vermesini sağlamak, kendileri hakkındaki iddialarını haklı çıklamak ister.')

tp2_col1.markdown(':red[Örnekler:] Paramahansa Yogananda, Papa John XXIII, Eleanor Roosevelt, Nancy Reagan, Monica Lewinsky, Leo Buscaglia, Luciano Pavarotti, Lionel Richie, Stevie Wonder, Elizabeth Taylor, Martin Sheen, Danny Glover,” Juliette Binoche')

tp2_col1.write('')
tp2_col1.write('')
tp2_col1.write('')

tp2_col1.markdown(':red[Bağımlılıklar]')

tp2_col1.markdown('Yiyecekleri ve reçetesiz satılan ilaçları kötüye kullanmak. Özellikle tatlılar ve karbonhidratlar üzerinde aşırı yeme. Aşırı durumlarda bulimiada "aşktan açlık" hissetmekten aşırı yemek. Sempati aramak için hipokondri.')

tp2_col2.subheader('Tip İki—Gelişim Düzeyleri')

tp2_col2.markdown(':red[Sağlıklı Seviyeler]')

tp2_col2.markdown(':red[Seviye 1 (En İyisi)]: Derinden bencil olmayan, alçakgönüllü ve özgecil olun: kendine ve başkalarına koşulsuz sevgi vermek. Başkalarının hayatlarında olmanın bir ayrıcalık olduğunu hissedin.')

tp2_col2.markdown(':red[Seviye 2]: Empatik, şefkatli, başkaları için duygu. İhtiyaçları hakkında önemsemek ve endişe duymak. Düşünceli, sıcak kalpli, bağışlayıcı ve samimi.')

tp2_col2.markdown(':red[Seviye 3]: Teşvik edici ve minnettar, başkalarındaki iyiyi görebilme. Hizmet önemlidir, ancak kendine de özen gösterir: besleyici, cömert ve veren, gerçekten sevgi dolu bir insan.')

tp2_col2.markdown(':red[Ortalama Seviyeler]')

tp2_col2.markdown(':red[Seviye 4]: Başkalarına daha yakın olmak istiyorum, bu yüzden "insanları memnun etmeye" başlayın, aşırı arkadaş canlısı, duygusal olarak gösterici ve her şey hakkında "iyi niyetlerle" dolu olun. Baştan çıkarıcı dikkat verin: onay, "vuruşlar", dalkavukluk. Aşk onların yüce değeridir ve sürekli bunun hakkında konuşurlar.')

tp2_col2.markdown(':red[Seviye 5]: Aşırı samimi ve müdahaleci olun: ihtiyaç duyulması gerekir, bu yüzden aşk adına süzülürler, müdahale ederler ve kontrol ederler. Başkalarının onlara bağımlı olmasını isteyin: verin, ancak bir geri dönüş bekleyin: çift mesaj gönderin. Zarflama ve sahiplenme: başkaları için yeterince yapamayan, bağımlı, fedakar kişi - herkes için kendilerini yıpratmak, kendileri için ihtiyaçlarını karşılamak.')

tp2_col2.markdown(':red[Seviye 6]: Giderek daha önemli ve kendinden tatmin olan, başkalarının adına çabalarını abartsalar da vazgeçilmez olduklarını hissederler. Hipokondri, başkaları için bir "şehit" olmak. Zorba, kibirli, küstah.')

tp2_col2.markdown(':red[Sağlıksız Seviyeler]')

tp2_col2.markdown(':red[Seviye 7]: Manipülatif ve kendi kendine hizmet edebilir, başkalarına onlara ne kadar borçlu olduklarını söyleyerek ve onlara acı çektirerek suçluluk aşılayabilir. Yiyecek ve ilaçları "duyguları doldurmak" ve sempati duymak için kötüye kullanın. İnsanları baltalamak, küçümseyici, aşamacı sözler yapmak. Güdüleri ve davranışlarının ne kadar agresif ve/veya bencil olduğu konusunda son derece kendi kendini aldatıcı.')

tp2_col2.markdown(':red[Seviye 8]: Egemen ve zorlayıcı: başkalarından istedikleri her şeyi almaya hak kazanın: eski borçların, paranın, cinsel iyiliklerin geri ödenmesi')

tp2_col2.markdown(':red[Seviye 9]: Başkaları tarafından istismar edildiğini ve mağdur olduklarını hissettikleri ve acı bir şekilde kırgın ve kızgın oldukları için yaptıklarını mazur gösterebilir ve rasyonelleştirebilir. Saldırganlıklarının somatizasyonu, "parçalanarak" ve başkalarına yük olarak kendilerini haklı çıkardıkları için kronik sağlık sorunlarına neden olur. Genellikle Histrionik Kişilik Bozukluğu ve Gerçeklü Bozukluğa karşılık gelir.')

tp2_col1.markdown(':red[Kişisel Gelişim Önerileri]')

tp2_col1.markdown('*Başkalarının ihtiyaçlarını karşılamadan önce iyi olduğunuzdan emin olmak bencilce değildir - bu sadece sağduyudur.')

tp2_col1.markdown('*İnsanlar için yapmak isteyebileceğiniz birçok şey olsa da, onlara önce gerçekten neye ihtiyaçları olduğunu sormak genellikle daha iyidir. Başkalarının duygularını ve ihtiyaçlarını doğru bir şekilde sezme konusunda yeteneklisiniz, ancak bu, bu ihtiyaçların sizin tarafınızdan aklınızda olduğu gibi giderilmesini istedikleri anlamına gelmez. Niyetinizi iletin ve "hayır teşekkür ederim"i kabul etmeye istekli olun. Özel yardım teklifinizi istemediğine karar veren biri, sizden hoşlanmadığı veya sizi reddettiği anlamına gelmez.')

tp2_col1.markdown('*Kendinize ve iyi işlerinize dikkat çekme cazibesine karşı durun. Başkaları için bir şey yaptıktan sonra, onlara bunu hatırlatmayın. Birakın: ya nezaketinizi kendileri hatırlayacaklar ve size kendi yollarıyla teşekkür edecekler ya da etmeyecekler. Onlar için yaptıklarınıza dikkat çekmeniz, insanları sadece yerinde koyar ve kendilerini tedirgin hissettirir.')

type_2.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)



type_3.header(':red[Başarı Odaklı]', divider='rainbow')

type_3.image('type3.gif', width=260)

type_3.subheader('Başarı Odaklı, Pragmatik Tip: Uyarlanabilir, Mükemmel, Yönlendirici ve Görüntü-Bilinçli')

tp3_col1, tp3_col2 = type_3.columns(2, gap='large')

tp3_col1.write('')

tp3_col1.subheader('Başarı Odaklı')


tp3_col1.markdown('Kendine güvenen, çekici ve çekicidir. Hırslı, yetkin ve enerjik, aynı zamanda statü-bilinçli ve ilerleme için yüksek oranda yönlendirilebilirler. Diplomatik ve denizlidirler, ancak imajlarıyla ve başkalarının onlar hakkında ne düşündüğüyle de aşırı derecede ilgilenebilirler. Genellikle işkoliklik ve rekabet gücü ile ilgili sorunları vardır. En iyi haliyle: kendini kabul eden, otantik, göründüğü her şey - başkalarına ilham veren rol modeller')

tp3_col1.markdown(':red[*Temel Korku]: Değersiz olmak')

tp3_col1.markdown(':red[*Temel Arzu]: Değerli hissetmek')

tp3_col1.markdown(':red[*Anahtar Motivasyonlar]: Onaylanmak, kendilerini başkalarından ayırt etmek, dikkat çekmek, hayran olmak ve başkalarını etkilemek ister.')

tp3_col1.markdown(':red[Örnekler:] Augustus Sezar, İmparator Constantin, Bill Clinton, Tony Blair, Prens William, Condoleeza Rice, Arnold Schwarzenegger, Carl Lewis, Muhammed Ali, Oprah Winfrey, Michael Jordan, O.J. Simpson, Tiger Woods, Lance Armstrong, Elvis Presley, Paul McCartney, Madonna, Sting, Whitney Houston, Jon Bon Jovi, Lady Gaga, Taylor Swift, Justin Bieber, Brooke Shields, Cindy Crawford, Tom Cruise, Barbra Streisand, Ben Kingsley, Jamie Foxx, Richard Gere, Will Smith, Courteney Cox, Demi Moore, Kevin Spacey, Reese Witherspoon, Anne Hathaway')

tp3_col1.write('')
tp3_col1.write('')
tp3_col1.write('')

tp3_col1.markdown(':red[Bağımlılıklar]')

tp3_col1.markdown('Tanınma için vücudu aşırı strese sokmak. Yorgunluk için çalışmak. Açlık diyetleri. İşkoliklik. Kozmetik iyileştirme için aşırı kahve, uyarıcılar, amfetaminler, kokain, steroidler veya aşırı cerrahi alımı.')


tp3_col2.subheader('Tip Üç—Gelişim Düzeyleri')

tp3_col2.markdown(':red[Sağlıklı Seviyeler]')

tp3_col2.markdown(':red[Seviye 1 (En İyisi)]: Kendini kabul eden, içsel-yönetilmiş ve otantik, göründüğü her şey. Mütevazı ve hayırsever, kendini küçücü mizah ve kalp doluluğu ortaya çıkar. Nazik ve yardımsever.')

tp3_col2.markdown(':red[Seviye 2]: Kendine güvenen, enerjik ve yüksek benlik saygısı ile yetkin: kendilerine ve kendi değerlerine inanırlar. Uyarlanabilir, arzu edilebilir, çekici ve zarif.')

tp3_col2.markdown(':red[Seviye 3]: Kendilerini geliştirmek, "olabileceklerinin en iyisi" olmak için hırslı - genellikle olağanüstü, insani bir ideal haline gelir, yaygın olarak beğenilen kültürel nitelikleri somutlaştırır. Son derece etkili: Diğerleri olumlu bir şekilde onlar gibi olmak için motive olur.')

tp3_col2.markdown(':red[Ortalama Seviyeler]')

tp3_col2.markdown(':red[Seviye 4]: Performanslarıyla son derece ilgili, işlerini iyi yapıyor, sanki self-worth buna bağlıymuş gibi hedeflere ulaşmak için sürekli kendini yönlendiriyor. Başarısızlıktan korktum. Statü ve başarı arayışında kendinizi başkalarıyla karşılaştırın. Kariyerci, sosyal tırmanıcı olun, münhasırlığa yatırım yapın ve "en iyi" olun.')

tp3_col2.markdown(':red[Seviye 5]: Nasıl algılandıklarıyla son derece ilgilenen, görüntü-bilinçli olun. Başkalarının beklentilerine ve başarılı olmak için ne yapmaları gerektiğine göre kendilerini paketlemeye başlayın. Pragmatik ve verimli, ancak aynı zamanda önceden planlanmış, pürüzsüz bir cephenin altında kendi duygularıyla temasını kaybeder. Yakınlık, güvenilirlik ve "sahtelik" ile ilgili sorunlar ortaya çıkar.')

tp3_col2.markdown(':red[Seviye 6]: Başkalarını üstünlükleriyle etkilemek istiyorum: kendilerini sürekli tanıtmak, kendilerini gerçekte olduklarından daha iyi tanıtmak. Narsist, görkemli, kendileri ve yetenekleri hakkında şişirilmiş kavramlar. Teşhirci ve baştan çıkarıcı, sanki "Bana bak!" diyormuş gibi Başkalarını küçümseme ve kibir, başkalarını kıskanmaya ve başarılarına karşı bir savunmadır.')

tp3_col2.markdown(':red[Sağlıksız Seviyeler]')

tp3_col2.markdown(':red[Seviye 7]: Başarısızlık ve aşağılanma korkusuyla, sömürücü ve fırsatçı olabilirler, başkalarının başarısına açık olabilirler ve üstünlüklerinin yanılsamasını korumak için "ne gerekiyorsa" yapmaya istekli olabilirler.')

tp3_col2.markdown(':red[Seviye 8]: Hataları ve yanlışları ortaya çıkmaması için dolambaçlı ve aldatıcı. Güvenilmez, kötü niyetli bir şekilde insanları üzmek veya onları zafererek sabote etmek. Başkalarını sanrılı bir şekilde kıskanıyor.')

tp3_col2.markdown(':red[Seviye 9]: Başkalarının mutluluğunu mahvetmeye çalışarak kindar olun. Acımasız, onlara kendi eksikliklerini ve başarısızlıklarını hatırlatan her şeyi yok etme konusunda takıntılı. Psikopatik davranış. Genellikle Narsistik Kişilik Bozukluğuna karşılık gelir.')

tp3_col1.write('')
tp3_col1.write('')

tp3_col1.markdown(':red[Kişisel Gelişim Önerileri]')

tp3_col1.markdown('*Gerçek gelişimimiz için doğru olmak şarttır. Gerçek duygularınız ve ihtiyaçlarınız hakkında kendinize ve başkalarına karşı dürüst olun. Aynı şekilde, başkalarını etkileme veya öneminizi şişirme cazibesine direnin')

tp3_col1.markdown('*Muhteşem bir şey gerekmez - sadece birkaç dakikalık sessiz yeterli. Bunu yaptığınızda, daha sevgi dolu bir insan, daha sadık bir arkadaş ve çok daha arzu edilen bir birey olacaksınız. Kendini daha iyi hissedeceksin.')

tp3_col1.markdown('*Mola ver. Hedeflerinizin amansız peşinde koşmanızla kendinizi ve başkalarını yorguna düşürebilirsiniz. Bazen pilinizi şarj etmek ve bakış açınızı iyileştirmek için üç ila beş derin nefes almak yeterlidir.')

type_3.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)





type_4.header(':red[Özgün-Bireyci]', divider='rainbow')

type_4.image('type4.gif', width=260)

type_4.subheader('Hassas, Introspektif Tip: Etkileyici, Dramatik, Bencil ve Mizaç')

tp4_col1, tp4_col2 = type_4.columns(2, gap='large')

tp4_col1.write('')

tp4_col1.subheader('Özgün')


tp4_col1.markdown('Öz farkındalıklı, hassas ve çekingendir. Duygusal olarak dürüst, yaratıcı ve kişiseldirler, ancak aynı zamanda karamsar ve öz-bilinçli olabilirler. Savunmasız ve kusurlu hissettikleri için kendilerini başkalarından alıkoyarak, aynı zamanda küçümseyici ve sıradan yaşam biçimlerinden muaf hissedebilirler. Genellikle melankoli, kendini beğenmişlik ve kendine acıma ile ilgili sorunları vardır. En iyileri: ilham verici ve son derece yaratıcı, kendilerini yenileyebilir ve deneyimlerini dönüştürebilirler.')

tp4_col1.markdown(':red[*Temel Korku]: Kimlikleri veya kişisel önemleri olmadığı')

tp4_col1.markdown(':red[*Temel Arzu]: Kendilerini ve önemlerini bulmak (bir kimlik)')

tp4_col1.markdown(':red[*Anahtar Motivasyonlar]: Kendilerini ve bireyselliklerini ifade etmek, kendilerini güzellikle yaratmak ve çevrelemek, belirli ruh hallerini ve duyguları korumak, kendi imajlarını korumak için geri çekilmek, başka bir şeye katılmadan önce duygusal ihtiyaçlarla ilgilenmek, bir "kurtarıcı" çekmek isterler.')

tp4_col1.markdown(':red[Örnekler:] Rumi, Frédéric Chopin, Pyotr I. Çaykovski, Jackie Kennedy Onassis, Edgar Allen Poe, Yukio Mishima, Virginia Woolf, Anne Frank, Tennessee Williams, J.D. Salinger, Anne Rice, Frida Kahlo, Maria Callas, Bob Dylan, Yusuf Islam (Cat Stevens), Ferron, Cher, Prince, Alanis Morrisette, Amy Winehouse, Ingmar Bergman, Marlon Brando, Jeremy Irons, Angelina Jolie, Winona Ryder, Kate Winslet, Nicolas Cage, Johnny Depp')

tp4_col1.write('')

tp4_col1.markdown(':red[Bağımlılıklar]')

tp4_col1.markdown('Ruh halini değiştirmek, sosyalleşmek ve duygusal teselli için zengin yiyeceklerde, tatlılarda, alkolde aşırı hoşgörü. Fiziksel aktivite eksikliği. Bulimia. Depresyon. Sosyal kaygı için tütün, reçeteli ilaçlar veya eroin. Reddedilen özellikleri silmek için kozmetik cerrahi.')


tp4_col2.subheader('Tip Dört—Gelişim Düzeyleri')

tp4_col2.markdown(':red[Sağlıklı Seviyeler]')

tp4_col2.markdown(':red[Seviye 1 (En İyisi)]: Son derece yaratıcı, kişisel ve evrensel olanı ifade eden, muhtemelen bir sanat eserinde. İlham verici, kendi kendini yenileyen ve yenileyen: tüm deneyimlerini değerli bir şeye dönüştürebilir: self-creative.')

tp4_col2.markdown(':red[Seviye 2]: Öz-farkında, içe dönük, "kendini arama" üzerine, duyguların ve içsel dürtülerin farkında. Hem kendine hem de başkalarına karşı hassas ve sezgisel: nazik, incelikli, şefkatli.')

tp4_col2.markdown(':red[Seviye 3]: Son derece kişisel, bireyci, "kendine sadık." Kendini açıklayan, duygusal olarak dürüst, insancıl. Benlik ve hayata ironik bakış: ciddi ve eğlenceli, savunmasız ve duygusal olarak güçlü olabilir.')

tp4_col2.markdown(':red[Ortalama Seviyeler]')

tp4_col2.markdown(':red[Seviye 4]: Kişisel duyguları geliştirmek ve uzatmak için güzel, estetik bir ortam yaratarak hayata sanatsal, romantik bir yönelim alın. Fantezi, tutkulu duygular ve hayal gücü ile gerçekliği artırın.')

tp4_col2.markdown(':red[Seviye 5]: Duygularla iletişimde kalmak için, her şeyi içselleştirirler, her şeyi kişisel olarak alırlar, ancak bencilleşirler ve içe dönükler, karamsarlar ve aşırı duyarlı, utangaç ve bilinçli olurlar, kendiliğinden olamazlar veya "kendilerinden çıkamazlar." Benlik imajlarını korumak ve duyguları çözmek için zaman satın almak için geri çekilmiş kalın.')

tp4_col2.markdown(':red[Seviye 6]: Yavaş yavaş diğerlerinden farklı olduklarını düşünür ve herkes gibi yaşamaktan muaf olduklarını hissederler. Bir fantezi dünyasında yaşayan melankolik hayalperestler, küçümseyici, çökmekte olan ve şehvetli olurlar. Kendine acıma ve başkalarının kıskançlığı, kendini beğenmişliğe ve giderek daha pratik olmayan, üretken olmayan, erimiş ve değerli hale gelmeye yol açar.')

tp4_col2.markdown(':red[Sağlıksız Seviyeler]')

tp4_col2.markdown(':red[Seviye 7]: Hayaller başarısız olduğunda, kendini engelleyen ve kendine kızar, depresif ve kendinden ve başkalarından yabancılaşır, engellenir ve duygusal olarak felç olur. Kendinden utanıyor, yorgun ve işlev göremiyor.')

tp4_col2.markdown(':red[Seviye 8]: Sanrısal kendini küçümseme, kendini serteme, kendinden nefret ve hastalıklı düşüncelerle işkence: her şey bir işkence kaynağıdır. Başkalarını suçlarak, onlara yardım etmeye çalışan herkesi uzaklaştırırlar.')

tp4_col2.markdown(':red[Seviye 9]: Umutsuzluk, umutsuz hissetme ve kendine zarar verme, muhtemelen kaçmak için alkol veya uyuşturucuyu kötüye kullanma. Aşırı: duygusal çöküş veya intihar muhtemeldir. Genellikle Kaçınan, Depresif ve Narsistik kişilik bozukluklarına karşılık gelir.')

tp4_col1.write('')

tp4_col1.markdown(':red[Kişisel Gelişim Önerileri]')

tp4_col1.markdown('*Duygularınıza çok fazla dikkat etmeyin; muhtemelen zaten bildiğiniz gibi, sizin için gerçek bir destek kaynağı değildirler. Duygularınızın size şu anda olduğu gibi kendiniz hakkında bir şey söylediğini hiç unutmayın, bundan fazlası değil.')

tp4_col1.markdown('*Çalışırken, yani potansiyellerinizi harekete geçirirken ve kendinizi gerçekleştirirken en mutlusunuz. Boşlukta veya ilhamın gelmesini beklerken "kendinizi bulmayacaksınız", bu yüzden gerçek dünyayla bağlantı kurun ve bağlantıda kalın.')

tp4_col1.markdown('*Özellikle olumsuz, kırgın ve hatta aşırı romantikse, hayal gücünüzde uzun konuşmalardan kaçının. Bu konuşmalar esasen gerçek dışıdır ve en iyi ihtimalle sadece eylem için provalardır - ancak bildiğiniz gibi, neredeyse hiç söyleyeceğinizi veya hayal ettiğiniz şeyi yapmazsınız. Hayatınızı ve ilişkilerinizi hayal etmek için zaman harcamak yerine, onları yaşamaya başlayın.')

type_4.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)




type_5.header(':red[Araştırmacı]', divider='rainbow')

type_5.image('type5.gif', width=260)

type_5.subheader('Yoğun, Serebral Tip: Algısal, Yenilikçi, Gizli ve İzole')

tp5_col1, tp5_col2 = type_5.columns(2, gap='large')

tp5_col1.write('')

tp5_col1.subheader('Araştırmacı')


tp5_col1.markdown('Uyanık, anlayışlı ve meraklı. Karmaşık fikirler ve beceriler geliştirmeye konsantre olabilirler ve odaklanabilirler. Bağımsız, yenilikçi ve yaratıcı, düşünceleri ve hayali yapılarıyla da meşgul olabilirler. Müstakil hale gelirler, ancak yüksek-stringng ve yoğun hale gelirler. Genellikle eksantriklik, nihilizm ve izolasyonla ilgili sorunları vardır. En İyileri: genellikle zamanlarının ötesinde ve dünyayı tamamen yeni bir şekilde görebilen vizyoner öncüler.')

tp5_col1.markdown(':red[*Temel Korku]: İşe yaramaz, çaresiz veya aciz olmak')

tp5_col1.markdown(':red[*Temel Arzu]: Yetenekli ve yetkin olmak')

tp5_col1.markdown(':red[*Anahtar Motivasyonlar]: Bilgiye sahip olmak, çevreyi anlamak, her şeyi çevreden gelen tehditlerden korumanın bir yolu olarak anlamak istiyorum.')

tp5_col1.markdown(':red[Örnekler:] Siddhartha Gautama Buddha, Albert Einstein, Stephen Hawking, Vincent van Gogh, Edvard Munch, Salvador Dali, Emily Dickinson, Friedrich Nietzsche, Agatha Christie, James Joyce, Jean-Paul Sartre, Stephen King, Ursula K. LeGuin, Bill Gates, Mark Zuckerberg, Kurt Cobain, Alfred Hitchcock, Stanley Kubrick, Tim Burton, Jodie Foster, Wikileaks Julian Assange')

tp5_col1.write('')
tp5_col1.write('')
tp5_col1.write('')

tp5_col1.markdown(':red[Bağımlılıklar]')

tp5_col1.markdown('İhtiyaçları en aza indirme nedeniyle kötü beslenme ve uyku alışkanlıkları. Hijyen ve beslenmeyi ihmal etmek. Fiziksel aktivite eksikliği. Zihinsel uyarım ve kaçış için psikotropik ilaçlar, anksiyete için narkotikler.')


tp5_col2.subheader('Tip Beş—Gelişim Düzeyleri')

tp5_col2.markdown(':red[Sağlıklı Seviyeler]')

tp5_col2.markdown(':red[Seviye 1 (En İyisi)]: Vizyoner olun, dünyayı derinlemesine nüfuz ederken geniş bir şekilde kavrayın. Açık fikirli, her şeyi gerçek bağlamlarında bütün olarak ele alın. Öncü keşifler yapın ve bir şeyler yapmanın ve algılamanın tamamen yeni yollarını bulun.')

tp5_col2.markdown(':red[Seviye 2]: Her şeyi olağanüstü algı ve içgörü ile gözlemleyin. Çoğu zihinsel olarak uyanık, meraklı, zeka arayan: hiçbir şey dikkatlerinden kaçamaz. Öngörü ve tahmin. Konsantre olabilme: dikkatlerini çeken şeye dalmış olmak.')

tp5_col2.markdown(':red[Seviye 3]:  İlgilerini çeken her şeyde ustaca ustalık elde edin. Bilgiden heyecanlanır: genellikle bazı alanlarda uzman olur. Yenilikçi ve yaratıcı, son derece değerli, özgün eserler üretiyor. Son derece bağımsız, kendine özgü ve tuhaf.')

tp5_col2.markdown(':red[Ortalama Seviyeler]')

tp5_col2.markdown(':red[Seviye 4]: Harekete geçmeden önce her şeyi kavramsallaştırmaya ve ince ayar yapmaya başlayın - zihinlerinde bir şeyleri çözer: model oluşturma, hazırlama, pratik yapma ve daha fazla kaynak toplama. Çalışkan, edinme tekniği. Uzmanlaşmış olun ve çoğu zaman "entelektüel" olun, genellikle kabul edilen bir şeyler yapma yollarına meydan okuyun.')

tp5_col2.markdown(':red[Seviye 5]: Karmaşık fikirlere veya hayali dünyalara dahil oldukça giderek daha fazla kopuk. Gerçeklikten ziyade vizyonları ve yorumlarıyla meşgul olun. Karanlık ve rahatsız edici unsurları içerenler bile, sıra dışı, ezoterik denekler tarafından büyülenirler. Pratik dünyadan kopuk, yüksek sinirli ve yoğun olmasına rağmen "bedensiz bir zihin".')

tp5_col2.markdown(':red[Seviye 6]: İç dünyalarına ve kişisel vizyonlarına müdahale edecek herhangi bir şeye karşı düşmanca bir duruş sergilemeye başlayın. Kasıtlı olarak aşırı ve radikal görüşlerle kışkırtıcı ve aşındırıcı olun. Alaycı ve tartışmacı.')

tp5_col2.markdown(':red[Sağlıksız Seviyeler]')

tp5_col2.markdown(':red[Seviye 7]: Gerçeklikten izole, eksantrik ve nihilist olun. Son derece dengesiz ve saldırganlıklardan korkarlar: başkalarını ve tüm sosyal bağları reddeder ve püskürtürler')

tp5_col2.markdown(':red[Seviye 8]: Takıntılı olun, ancak tehdit edici fikirlerinden korkun, dehşete düşün, çılgın ve büyük çarpıtmalara ve fobilere av olur.')

tp5_col2.markdown(':red[Seviye 9]: Aşırılma arayışında, intihar edebilir veya gerçeklikle psikotik bir kopuş yaşayabilirler. Derange, patlayıcı bir şekilde kendi kendini yok eden, şizofrenik tonlarla. Genellikle Şizoid Kaçınma ve Şizotipal kişilik bozukluklarına karşılık gelir.')

tp5_col1.write('')
tp5_col1.write('')
tp5_col1.write('')

tp5_col1.markdown(':red[Kişisel Gelişim Önerileri]')

tp5_col1.markdown('*Zihinsel kapasiteleriniz olağanüstü bir hediye olabilir, ancak yalnızca kendinizle ve başkalarıyla temastan geri çekilmek için kullandığınızda da bir tuzak olabilir. Fizikselliğinizle bağlantıda kalın.')

tp5_col1.markdown('*Son derece yoğun ve o kadar güçlü olma eğilimindesiniz ki, rahatlamak ve gevşemekte zorlanırsınız. Uyuşturucu veya alkol olmadan sağlıklı bir şekilde sakinleşmeyi öğrenmek için çaba gösterin.')

tp5_col1.markdown('*Beşler, insanlara güvenmeyi, onlara duygusal olarak açılmayı veya kendilerini çeşitli şekillerde erişilebilir kılmayı zor bulma eğilimindedir. Çatışmalar yaşayacak kadar güvendiğiniz bir veya iki yakın arkadaşınıza sahip olmak hayatınızı büyük ölçüde zenginleştirecektir.')

type_5.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)




type_6.header(':red[Sadık]', divider='rainbow')

type_6.image('type6.gif', width=260)

type_6.subheader('Taahhütlü, Güvenlik Odaklı Tür: İlgi Çekici, Sorumlu, Endişeli ve Şüpheli')

tp6_col1, tp6_col2 = type_6.columns(2, gap='large')

tp6_col1.write('')

tp6_col1.subheader('Sadık')


tp6_col1.markdown('Kararlı, güvenlik odaklı tip. Sixes güvenilir, çalışkan, sorumlu ve güvenilirdir. Mükemmel "sorun gidericiler", sorunları öngörürler ve işbirliğini teşvik ederler, ancak aynı zamanda savunmacı, kaçamak ve endişeli olabilirler - şikayet ederken strese koşarlar. Temkinli ve kararsız olabilirler, aynı zamanda reaktif, meydan okuyan ve isyankar olabilirler. Genellikle kendinden şüphe ve şüphe ile ilgili sorunları vardır. En iyi ihtimalle: içsel olarak istikrarlı ve kendine güvenen, kendilerini ve başkalarını cesurca savunuyorlar.')

tp6_col1.markdown(':red[*Temel Korku]: Desteksiz ve rehberliksiz olma')

tp6_col1.markdown(':red[*Temel Arzu]: Güvenlik ve desteğe sahip olmak')

tp6_col1.markdown(':red[*Anahtar Motivasyonlar]: Güvenliğe sahip olmak, başkaları tarafından desteklendiğini hissetmek, kesinlik ve güvenceye sahip olmak, başkalarının onlara karşı tutumlarını test etmek, kaygı ve güvensizliğe karşı savaşmak istemek.')

tp6_col1.markdown(':red[Örnekler:] Mark Twain, Sigmund Freud, Richard Nixon, Robert F. Kennedy, Malcolm X, George H.W. Bush, Galler Prensesi Diana, Prens Harry, J.R.R. Tolkien, John Grisham, Mike Tyson, U2s Bono, Eminem, Oliver Stone, Marilyn Monroe, Robert De Niro, Dustin Hoffman, Mark Wahlberg, Woody Allen, Diane Keaton, Mel Gibson, Tom Hanks, Meg Ryan, Julia Roberts, Jennifer Aniston, Sarah Jessica Parker, Ben Affleck, Katie Holmes, David Letterman, Jay Leno, Ellen Degeneres, Chris Rock')

tp6_col1.write('')
tp6_col1.write('')
tp6_col1.write('')

tp6_col1.markdown(':red[Bağımlılıklar]')

tp6_col1.markdown('Diyetteki sertlik, beslenme dengesizliklerine neden olur ("Sebzeleri sevmiyorum"). Aşırı çalışmak. Dayanıklılık için kafein ve amfetaminler, aynı zamanda anksiyeteyi azaltmak için alkol ve depresanlar. Alkolizme karşı birçok türden daha yüksek duyarlılık.')


tp6_col2.subheader('Tip Altı—Gelişim Düzeyleri')

tp6_col2.markdown(':red[Sağlıklı Seviyeler]')

tp6_col2.markdown(':red[Seviye 1 (En İyisi)]: Kendini onaylayan, kendine ve başkalarına güvenen, bağımsız ancak simbiyotik olarak birbirine bağımlı ve eşit olarak işbirlikçi olun. Benliğe olan inanç, gerçek cesarete, olumlu düşünmeye, liderliğe ve zengin kendini ifade etmeye yol açar.')

tp6_col2.markdown(':red[Seviye 2]: Başkalarından güçlü duygusal tepkiler ortaya çıkarabilir: çok çekici, sevimli, sevimli, sevecen. Güven önemli: başkalarıyla bağ kurmak, kalıcı ilişkiler ve ittifaklar kurmak.')

tp6_col2.markdown(':red[Seviye 3]: Derinden inandıkları bireylere ve hareketlere adanmıştır. Topluluk oluşturucular: sorumlu, güvenilir, güvenilir. Çalışkan ve sebatlı, başkaları için fedakarlık yaparak, dünyalarında istikrar ve güvenlik yaratır, işbirlikçi bir ruh getirir.')

tp6_col2.markdown(':red[Ortalama Seviyeler]')

tp6_col2.markdown(':red[Seviye 4]: Zamanlarını ve enerjilerini güvenli ve istikrarlı olacağına inandıkları her şeye yatırmaya başlayın. Örgütlemek ve yapılandırmak, güvenlik ve süreklilik için ittifaklara ve yetkililere bakarlar. Sürekli uyanık, sorunları tahmin etmek.')

tp6_col2.markdown(':red[Seviye 5]: Onlardan daha fazla talepte bulunulmasına direnmek için, başkalarına karşı pasif-agresif bir şekilde tepki verirler. Kaçamak, kararsız, temkinli, erteleyici ve kararsız olun. Oldukça reaktif, endişeli ve olumsuz, çelişkili, "karışık sinyaller" veriyor. İç karışıklık, tahmin edilemez tepki vermelerini sağlar.')

tp6_col2.markdown(':red[Seviye 6]: Güvensizlikleri telafi etmek için alaycı ve savaşçı hale gelirler, sorunları için başkalarını suçlarlar, "yabancılara" karşı sert bir duruş sergilerler. Son derece reaktif ve savunmacı, kendi güvenliklerine yönelik tehditler ararken insanları arkadaşlara ve düşmanlara bölüyor. Otoriteden korkarken otoriter, son derece şüpheli, ancak komplocu ve kendi korkularını susturmak için korku')

tp6_col2.markdown(':red[Sağlıksız Seviyeler]')

tp6_col2.markdown(':red[Seviye 7]: Güvenliklerini mahvettiklerinden korkarak, akut aşağılık duygularıyla panik, değişken ve kendini aşağılayan hale gelirler. Kendilerini savunmasız olarak görerek, tüm sorunları çözmek için daha güçlü bir otorite veya inanç ararlar. Son derece bölücü, başkalarını küçümse ve azarlama.')

tp6_col2.markdown(':red[Seviye 8]: Zulme uğradığını, başkalarının "onları almak için dışarıda" olduğunu hissederler, sertler ve mantıksız davranırlar, korktukları şeyi getirirler. Fanatizm, şiddet.')

tp6_col2.markdown(':red[Seviye 9]: Histerik ve cezadan kaçmaya çalışarak kendi kendine zarar verici ve intihara meyilli hale gelirler. Alkolizm, aşırı dozda uyuşturucu, kendini azalayan davranış. Genellikle Pasif-Agresif ve Paranoyak kişilik bozukluklarına karşılık gelir.')

tp6_col1.write('')
tp6_col1.write('')
tp6_col1.write('')

tp6_col1.markdown(':red[Kişisel Gelişim Önerileri]')

tp6_col1.markdown('*Altılılar stres altında olduklarında ve endişeli hissettiklerinde aşırı tepki verme eğilimindedir. Sizi neyin aşırı tepki verdiğini belirlemeyi öğrenin. Ayrıca, bu kadar çok korktuğunuz şeylerin neredeyse hiçbirinin gerçekten gerçekleşmediğini anlayın.')

tp6_col1.markdown('*Hayatınızda şüphesiz sizi önemseyen ve güvenilir olan birkaç kişi var. Değilse, güvenilir birini bulmak için elinizden geleni yapın ve o kişiye yaklaşmanıza izin verin. Bu, reddedilmeyi riske atmak ve en derin korkularınızdan bazılarını karıştırmak anlamına gelir, ancak risk almaya değer.')

tp6_col1.markdown('*İlişkilerinizde çitin bir tarafında veya diğerinde net bir şekilde aşağı inin. İnsanlara onlar hakkında ne hissettiğinizi bildirin.')

type_6.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)





type_7.header(':red[Maceracı]', divider='rainbow')

type_7.image('type7.gif', width=260)

type_7.subheader('Meşgul, Çeşitlilik Arayan Tür: Spontan, Çok Yönlü, Edinici ve Dağınık')

tp7_col1, tp7_col2 = type_7.columns(2, gap='large')

tp7_col1.write('')

tp7_col1.subheader('Maceracı')


tp7_col1.markdown('Dışa dönük, iyimser, çok yönlü ve kendiliğinden. Oynak, yüksek ruhlu ve pratik, aynı zamanda birçok yeteneklerini yanlış uygulayabilir, aşırı geniş, dağınık ve disiplinsiz hale gelebilirler. Sürekli olarak yeni ve heyecan verici deneyimler ararlar, ancak hareket halindeyken dikkatleri dağılabilir ve tükenebilirler. Genellikle sabırsızlık ve dürtüsellik ile ilgili sorunları vardır. En iyi şekilde: yeteneklerini değerli hedeflere odaklarlar, minnettar, neşeli ve tatmin olurlar.')

tp7_col1.markdown(':red[*Temel Korku]: Yoksul ve acı çekme')

tp7_col1.markdown(':red[*Temel Arzu]: Tatmin olmak ve memnun olmak—ihtiyaçlarının karşılanması')

tp7_col1.markdown(':red[*Anahtar Motivasyonlar]: Özgürlüklerini ve mutluluklarını korumak, değerli deneyimleri kaçırmamak, kendilerini heyecanlı ve meşgul tutmak, acıdan kaçınmak ve boşaltmak isterler.')

tp7_col1.markdown(':red[Örnekler:] Galileo Galilei, W.A. Mozart, Thomas Jefferson, Benjamin Franklin, John F. Kennedy, Joe Biden, Sarah Palin, Silvio Berlusconi, Malcolm Forbes, Richard Branson, Elton John, Mick Jagger, Miley Cyrus, Britney Spears, Katy Perry, Steven Spielberg, John Belushi, George Clooney, Brad Pitt, Williams Robin, Jim Carrey, Bruce Willis, Robert Downey, Jr.')

tp7_col1.write('')

tp7_col1.markdown(':red[Bağımlılıklar]')

tp7_col1.markdown('Bağımlılığa en yatkın tip: uyarıcılar (kafein, kokain ve amfetaminler), Ecstasy, psikotropikler, narkotikler ve alkol, ancak diğer depresanlardan kaçınma eğilimindedir. "Ayakta" kalmak için çabayla vücudu yıpratın. Aşırı kozmetik cerrahi, ağrı kesiciler.')


tp7_col2.subheader('Tip Yedi—Gelişim Düzeyleri')

tp7_col2.markdown(':red[Sağlıklı Seviyeler]')

tp7_col2.markdown(':red[Seviye 1 (En İyisi)]: Deneyimleri derinlemesine özümseyin, sahip oldukları için derinden minnettar ve minnettar olmalarını sağlayın. Hayatın basit harikalarından hayretli olun: neşeli ve kendinden geçmiş. Manevi gerçekliğin, yaşamın sınırsız iyiliğinin imaları.')

tp7_col2.markdown(':red[Seviye 2]: Son derece duyarlı, heyecan verici, sansasyon ve deneyim konusunda hevesli. En dışa dönük tip: uyaranlar anında tepki getirir - her şeyi canlandırıcı bulurlar. Canlı, canlı, istekli, spontane, dayanıklı, neşeli.')

tp7_col2.markdown(':red[Seviye 3]: Kolayca başarılı başarılılar, birçok farklı şeyi iyi yapan genelciler olun: multi-talented. Pratik, üretken, genellikle üretken, çapraz gübreleyici ilgi alanları.')

tp7_col2.markdown(':red[Ortalama Seviyeler]')

tp7_col2.markdown(':red[Seviye 4]: Huzursuzluk arttıkça, daha fazla seçenek ve seçeneğe sahip olmak ister. Maceracı ve "dünyevi bilge" olun, ancak daha az odaklı olun, sürekli yeni şeyler ve deneyimler arar: sofistike, uzman ve tüketici. Para, çeşitlilik, en son trendlere ayak uydurmak önemlidir.')

tp7_col2.markdown(':red[Seviye 5]: Gerçekten neye ihtiyaç duyduklarını ayırt edemiyorlar, hiperaktif oluyorlar, kendilerine "hayır" diyemiyorlar, kendilerini sürekli aktiviteye atıyorlar. Kısıtsız, aklıma gelen her şeyi yapmak ve söylemek: hikaye anlatımı, gösterişli abartılar, esprili bilge-cracking, performans. Sıkılmaktan korku: sürekli hareket halinde, ancak çok fazla şey yapın - birçok fikir ama çok az takip eder.')

tp7_col2.markdown(':red[Seviye 6]: Göze çarpan tüketime ve her türlü fazlalığa girin. Benmerkezci, materyalist ve açgözlü, asla yeterince sahip olduklarını hissetmezler. Talepkar ve saldırgan, ancak tatminsiz ve yorgun. Bağımlılık yapan, sertleşmiş ve duyarsız.')

tp7_col2.markdown(':red[Sağlıksız Seviyeler]')

tp7_col2.markdown(':red[Seviye 7]: Endişelerini bastırmak için çaresiz, dürtüsel ve çocukça olabilir: ne zaman duracağını bilmiyorum. Bağımlılıklar ve fazlalıklar bedelini öder: sefah, ahlaksız, dağılmış kaçanlar, saldırgan ve tacizci.')

tp7_col2.markdown(':red[Seviye 8]: Kendinden kaçarken, kaygı veya hayal kırıklıklarıyla uğraşmak yerine dürtüleri harekete geçirin: kontrolden çıkın, düzensiz ruh hali değişimlerine ve kompulsif eylemlere (manialar) gidin.')

tp7_col2.markdown(':red[Seviye 9]: Son olarak, enerjileri ve sağlıkları tamamen harcanır: klostrofobik ve panik-hatle olur. Genellikle kendilerinden ve yaşamdan vazgeçerler: derin depresyon ve umutsuzluk, kendi kendine yıkıcı aşırı dozlar, dürtüsel intihar. Genellikle Bipolar bozukluk ve Histrionik kişilik bozukluğuna karşılık gelir.')

tp7_col1.write('')

tp7_col1.markdown(':red[Kişisel Gelişim Önerileri]')

tp7_col1.markdown('*Dürtüselliğinizi tanıyın ve onlara teslim olmak yerine dürtülerinizi gözlemleme alışkanlığı edinin. Bu, dürtülerinizin çoğunun geçmesine izin vermek ve hangilerinin harekete geçmeye değer olduğunu daha iyi bir yargılamak anlamına gelir. Dürtülerinizi harekete geçirmeye ne kadar çok karşı koyabilirseniz, sizin için gerçekten neyin iyi olduğuna o kadar çok odaklanabileceksiniz.')

tp7_col1.markdown('*Diğer insanları dinlemeyi öğrenin. Genellikle ilginçtirler ve size yeni kapılar açacak şeyler öğrenebilirsiniz. Ayrıca sessizliği ve yalnızlığı takdir etmeyi öğrenin')

tp7_col1.markdown('*Şu anda her şeye sahip olmak zorunda değilsin. Bu cazip yeni satın alma büyük olasılıkla yarın hala mevcut olacak (bu kesinlikle gıda, alkol ve diğer yaygın tatminler için geçerlidir - örneğin dondurma külahı). Çoğu iyi fırsat tekrar geri gelecek ve hangi fırsatların sizin için gerçekten en iyi olduğunu ayırt etmek için daha iyi bir konumda olacaksınız.')

type_7.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)




type_8.header(':red[Meydan Okuyan]', divider='rainbow')

type_8.image('type8.gif', width=260)

type_8.subheader('Güçlü, Baskın Tip: Kendine Güvenen, Kararlı, Kasıtlı ve Çatışmacı')

tp8_col1, tp8_col2 = type_8.columns(2, gap='large')

tp8_col1.write('')

tp8_col1.subheader('Meydan Okuyan')


tp8_col1.markdown('kendine güvenen, güçlü ve iddialıdır. Koruyucu, becerikli, düz konuşan ve kararlı, ancak aynı zamanda ego merkezli ve otoriter olabilir. Sekizler, çevrelerini, özellikle de insanları kontrol etmeleri gerektiğini, bazen çatışmacı ve korkutucu hale geldiklerini düşünüyor. Sekizlerin tipik olarak öfkeleri ve savunmasız olmalarına izin vermeleri ile ilgili sorunları vardır. En iyi hallerinde: self- mastering, güçlerini başkalarının hayatlarını iyileştirmek, kahramanca, cömert ve ilham verici olmak için kullanırlar.')

tp8_col1.markdown(':red[*Temel Korku]: Başkaları tarafından zarar görmek veya kontrol edilmek')

tp8_col1.markdown(':red[*Temel Arzu]: Kendilerini korumak ve kendi hayatlarını kontrol altında tutmak')

tp8_col1.markdown(':red[*Anahtar Motivasyonlar]: Kendine güvenmek, güçlerini kanıtlamak ve zayıflığa direnmek, dünyalarında önemli olmak, çevreye hükmetmek ve durumlarını kontrol altında kalmak ister.')

tp8_col1.markdown(':red[Örnekler:] Richard Wagner, Franklin D. Roosevelt, Winston Churchill, Oskar Schindler, Fidel Castro, Hitler, Martin Luther King, Jr., Lyndon Johnson, Mikhail Gorbachev, Golda Meir, Indira Gandhi, Saddam Hussein, Donald Trump, Pablo Picasso, Ernest Hemingway, Serena Williams, Queen Latifah, Pink, John Wayne, Frank Sinatra, Humphrey Bogart, Sean Connnery, Paul Newman, Clint Eastwood, Tommy Lee Jones, Jack Nicholson, Susan Sarandon, Russell Crowe, Sean Penn, Matt Damon, Alec Baldwin, “Tony Soprano"')


tp8_col1.markdown(':red[Bağımlılıklar]')

tp8_col1.markdown('Fiziksel ihtiyaçları ve sorunları görmezden gelin: tıbbi ziyaretlerden ve check-uplardan kaçının. Kendini çok zorlarken zengin gıdalar, alkol, tütün tüketmek yüksek strese, felçlere ve kalp rahatsızlıklarına yol açar. Alkolizm ve narkotik bağımlılıklar mümkün olsa da, kontrol merkezi sorunlar.')


tp8_col2.subheader('Tip Sekiz—Gelişim Düzeyleri')

tp8_col2.markdown(':red[Sağlıklı Seviyeler]')

tp8_col2.markdown(':red[Seviye 1 (En İyisi)]: Kendini kısıtlayan ve cömert, merhametli ve hoşgörülü olun, daha yüksek bir otoriteye teslim olma yoluyla kendine hakim olun. Cesur, vizyonlarını gerçekleştirmek için kendini ciddi bir tehlikeye sokmaya istekli ve kalıcı bir etkiye sahip. Gerçek kahramanlığa ve tarihsel büyüklüğe ulaşabilir')

tp8_col2.markdown(':red[Seviye 2]: Kendine güvenen, kendine güvenen ve güçlü: ihtiyaç duydukları ve istedikleri şey için ayağa kalkmayı öğrendiler. Becerikli, "yapabilir" bir tutum ve tutkulu bir iç dürtü.')

tp8_col2.markdown(':red[Seviye 3]: Kararlı, otoriter ve komuta edici: diğerlerinin baktığı doğal lider. İnisiyatif alın, bir şeyler yapın: insanları şampiyon, sağlayıcı, koruyucu ve onurlu, güçlerini ile başkalarını taşıyın.')

tp8_col2.markdown(':red[Ortalama Seviyeler]')

tp8_col2.markdown(':red[Seviye 4]: Kendi kendine yeterlilik, finansal bağımsızlık ve yeterli kaynağa sahip olmak önemli endişelerdir: girişimci, pragmatik, "sağlam bireyciler", tekerlekli satıcılar olmak. Risk alma, çalışkan, kendi duygusal ihtiyaçlarını inkar etmek.')

tp8_col2.markdown(':red[Seviye 5]: Diğerleri de dahil olmak üzere çevrelerine hükmetmeye başlayın: başkalarının arkalarında olduğunu hissetmek ve çabalarını desteklemek istemek. Sert serilenen, övünen, güçlü ve geniş: sözü yasa olan "patron". Gururlu, benmerkezci, başkalarını eşit olarak görmemek veya onlara saygılı davranmamak için her şeye iradelerini ve vizyonlarını empoze etmek ister.')

tp8_col2.markdown(':red[Seviye 6]: Yollarını elde etmek için son derece kavgacı ve korkutucu olun: çatışmacı, savaşçı, düşmanca ilişkiler kurmak. Her şey bir irade testi ve geri adım atmayacaklar. Başkalarından itaat almak, başkalarını dengeden uzak ve güvensiz tutmak için tehditler ve misillemeler kullanın. Bununla birlikte, adaletsiz muamele, başkalarını korkutur ve onlardan içerler, muhtemelen onlara karşı da bir araya gelir.')

tp8_col2.markdown(':red[Sağlıksız Seviyeler]')

tp8_col2.markdown(':red[Seviye 7]: Onları kontrol etmek için herhangi bir girişime meydan okumak, tamamen acımasız, diktatör olmak, "kudidi doğru yapar." Suçlu ve kanun kaçağı, renegade ve con-artist. Sert kalpli, ahlaksız ve potansiyel olarak şiddetli.')

tp8_col2.markdown(':red[Seviye 8]: Güçleri, yenilmezlikleri ve galip gelme yetenekleri hakkında sanrısal fikirler geliştirin: megalomani, her şeye gücü yeten, yenilmez hissetme. Pervasızca aşırı genişleyen benlik.')

tp8_col2.markdown(':red[Seviye 9]: Tehlikeye girerlerse, başkasına teslim olmak yerine iradelerine uymayan her şeyi vahşice yok edebilirler. Vengeful, barbar, katil. Sosyopatik eğilimler. Genellikle Antisosyal Kişilik Bozukluğuna karşılık gelir.')


tp8_col1.markdown(':red[Kişisel Gelişim Önerileri]')

tp8_col1.markdown('*Gerçek gücünüz, insanlara ilham verme ve onları yükseltme yeteneğinizde yatmaktadır. Sorumluluğu üstlendiğinizde ve bir krizde herkese yardım ettiğinizde en iyi durumdasınız')

tp8_col1.markdown('*Çoğu zaman, çok az şey gerçekten tehlikededir ve gücünüzü veya gerçek ihtiyaçlarınızı feda etme korkusu olmadan başkalarının kendi yollarına gitmesine izin verebilirsiniz. Her zaman herkese hükmetme arzusu, egonuzun şişirmeye başladığının bir işaretidir - başkalarıyla daha ciddi çatışmaların kaçınılmaz olduğunun bir tehlike işaretidir.')

tp8_col1.markdown('*Sekizler genellikle kendine güvenmek ister ve kimseye bağımlı değildir. Ancak ironik bir şekilde, birçok insana bağlılar. Örneğin, işleri için size bağlı oldukları için çalışanlarınıza bağımlı olmadığınızı düşünebilirsiniz. Onları istediğiniz zaman işten çıkarabilir ve diğer işçileri işe alabilirsiniz. Siz hariç, küçük krallığınızda herkes harcanabilir. Ancak gerçek şu ki, özellikle iş endişeleriniz tek başına yönetebileceğinizin ötesinde büyürse, işlerini yapmak için başkalarına da bağımlısınız. Ancak sizinle ilişkili herkesi yabancılaştırırsanız, sonunda en beceriksiz ve güvenilmez kişileri işe almak zorunda kalırsınız. Bunu yaptığınızda, sadakatlerini sorgulamak ve konumunuzu kaybetmekten korkmak için nedeniniz olacak. Gerçek şu ki, ister iş dünyanızda ister ev hayatınızda olsun, kendi kendine yeterliliğiniz büyük ölçüde bir yanılsamadır.')

type_8.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)





type_9.header(':red[Barışçı]', divider='rainbow')

type_9.image('type9.gif', width=260)

type_9.subheader('Kolay Geçinilen, Alçakgönüllü Tip:Alıcı, Güven Verici Kabul Edilebilir ve Halinden Memnun')

tp9_col1, tp9_col2 = type_9.columns(2, gap='large')

tp9_col1.write('')

tp9_col1.subheader('Barışçı')


tp9_col1.markdown('Kolay anlaşılabilir, güvenilir ve istikrarlı. Genellikle yaratıcı, iyimser ve destekleyicidirler, ancak aynı zamanda barışı korumak için başkalarıyla birlikte gitmeye çok istekli olabilirler. Her şeyin sorunsuz gitmesini ve çatışmasız olmasını istiyorlar, ancak aynı zamanda şikayetçi olma, sorunları basitleştirme ve üzücü her şeyi en aza indirme eğiliminde olabilirler. Genellikle atalet ve inatçılık ile ilgili sorunları vardır. En iyi ihtimalle: yılmaz ve her şeyi kucaklayan, insanları bir araya getirebilir ve çatışmaları iyileştirebilirler.')

tp9_col1.markdown(':red[*Temel Korku]: Kayıp ve ayrılık')

tp9_col1.markdown(':red[*Temel Arzu]:  İçsel istikrara sahip olmak "zihin huzuru"')

tp9_col1.markdown(':red[*Anahtar Motivasyonlar]: Çevrelerinde uyum yaratmak, çatışmalardan ve gerilimden kaçınmak, şeyleri olduğu gibi korumak, onları üzecek veya rahatsız edecek her şeye direnmek ister.')

tp9_col1.markdown(':red[Örnekler:] Kraliçe II. Elizabeth, Monako Prensesi Grace, Abdullah Gül, Claude Monet, Abraham Lincoln, Dwight D. Eisenhower, Gerald Ford, Ronald Reagan, George W. Bush, John F. Kennedy, Jr., Carl Jung, Walt Disney, Ringo Starr, Carlos Santana, James Taylor, Janet Jackson, Jack Johnson, George Lucas, Ron Howard, Gary Cooper, Jimmy Stewart, Audrey Hepburn, Sophia Loren, Kevin Costner, Annette Bening, Jeff Bridges, Morgan Freeman, John Goodman, Matthew Broderick, , Lisa Kudrow, ” “Homer and Marge Simpson"')

tp9_col1.markdown(':red[Bağımlılıklar]')

tp9_col1.markdown('Öz farkındalık eksikliği ve bastırılmış öfke nedeniyle aşırı yemek veya az yemek. Fiziksel aktivite eksikliği. Depresanlar ve psikotropikler, alkol, esrar, yalnızlığı ve kaygıyı azaltmak için narkotikler.')


tp9_col2.subheader('Tip Dokuz—Gelişim Düzeyleri')

tp9_col2.markdown(':red[Sağlıklı Seviyeler]')

tp9_col2.markdown(':red[Seviye 1 (En İyisi)]: Kendine sahip olun, özerk ve tatmin edici hissedin: kendilerine mevcut oldukları için büyük bir eşitlik ve memnuniyete sahip olun. Paradoksal olarak, benlikle bir ve böylece daha derin ilişkiler kurabilir. Yoğun bir şekilde canlı, kendine ve başkalarına tamamen bağlı.')

tp9_col2.markdown(':red[Seviye 2]: Derinden alıcı, kabul edici, bilinçsiz, duygusal olarak istikrarlı ve sakin. Kendine ve başkalarına güvenmek, kendine ve yaşamla rahat, masum ve basit. Sabırlı, iddiasız, iyi-huylu, gerçekten iyi insanlar.')

tp9_col2.markdown(':red[Seviye 3]: İyimser, güven verici, destekleyici: iyileştirici ve sakinleştirici bir etkiye sahip olmak—grupları uyumlu hale getirmek, insanları bir araya getirmek: iyi bir arabulucu, sentezleyici ve iletişimci.')

tp9_col2.markdown(':red[Ortalama Seviyeler]')

tp9_col2.markdown(':red[Seviye 4]: Korku çatışmaları, bu yüzden kendini söven ve uzlaşmacı olun, başkalarını idealize edin ve gerçekten yapmak istemedikleri şeylere "evet" diyerek isteklerine "uyun" olun. Geleneksel rollere ve beklentilere düşer. Başkalarını saptırmak için felsefeleri ve hisse senedi sözlerini kullanın.')

tp9_col2.markdown(':red[Seviye 5]: Aktif, ancak ilgisiz, yansımasız ve dikkatsiz. Etkilenmek istemiyorum, bu yüzden tepkisiz ve rehavetsiz olun, sorunlardan uzaklaşın ve "onları halının altına süpürün." Düşünme, gerçekliği "ayarlamaya" başladıklarında, habersiz hale geldiklerinde, puslu ve geviş getiren, çoğunlukla rahatlatıcı fanteziler haline gelir. Duygusal olarak uyuşuk, kendini zorlama veya sorunlara odaklanma isteksizliği: kayıtsızlık.')

tp9_col2.markdown(':red[Seviye 6]: Sorunları en aza indirmeye, başkalarını yatıştırmaya ve "ne pahasına olursa olsun barış" için başlayın. Bir şeyi değiştirmek için hiçbir şey yapılamazmış gibi inatçı, kaderci ve istifa etti. Düsenekli düşünceye ve büyülü çözümlere. Diğerleri ertelemeleri ve tepkisizlikleriyle hüsrana uğramış ve kızmış.')

tp9_col2.markdown(':red[Sağlıksız Seviyeler]')

tp9_col2.markdown(':red[Seviye 7]: Oldukça bastırılmış, gelişmemiş ve etkisiz olabilir. Sorunlarla yüzleşmekten aciz hissedin: inatçı olun, kendini tüm çatışmalardan ayırın. Başkaları için ihmalkar ve tehlikeli.')

tp9_col2.markdown(':red[Seviye 8]: arkındalığı onları etkileyebilecek herhangi bir şeyi engellemek istiyorlar, o kadar çok ayrışıyorlar ki sonunda işlev göremiyorlar: uyuşmuş, kişiliksizleştirilmiş.')

tp9_col2.markdown(':red[Seviye 9]: Sonunda ciddi şekilde şaşırmış ve katatonik hale gelirler, kendilerini terk ederler, paramparça edilmiş kabuklara dönüşürler. Birden fazla kişilik mümkün. Genellikle Şizoid ve Bağımlı kişilik bozukluklarına karşılık gelir')


tp9_col1.markdown(':red[Kişisel Gelişim Önerileri]')

tp9_col1.markdown('*Başkalarının isteklerini sürekli olarak kabul etmek, sizi gerçekten tatmin edecek türden ilişkiler sağlayacak mı? Unutmayın, onlara gerçekten hazır değilseniz, başkalarını sevmek imkansızdır. Bu, kendiniz olmanız gerektiği, (paradoksal olarak) bağımsız olmanız gerektiği anlamına gelir, böylece size ihtiyaç duyduklarında başkalarının yanında olabilirsiniz.')

tp9_col1.markdown('*Bu sizin için çok acı verici olacak olsa da, evliliğiniz boşanmayla sonuçlandıysa veya çocuklarınızla ilgili sorun yaşıyorsanız, bu sorunlara nasıl katkıda bulunduğunuzu dürüstçe incelemelisiniz. Sorunlu ilişkileri incelemek son derece zor olacaktır çünkü ilgili insanlar kalbinize yakın olmuştur. Başkalarına karşı sahip olduğunuz duygular size kimliğinizin ve benlik saygınızın çoğunu bağlar. Ancak başkalarını gerçekten seviyorsanız, ortaya çıkan çatışmalarda oynadığınız rolü incelemekten daha azını yapamazsınız. Son analizde, seçim basittir: gerçek ilişkilerin (uzun vadede) tatmini için (kısa vadede) iç huzurunuzu feda etmelisiniz.')

tp9_col1.markdown('*Vücudunuzun ve duygularınızın daha fazla farkına varmak için sık sık egzersiz yapın. Düzenli egzersiz, sağlıklı bir öz disiplin şeklidir ve duygularınız ve diğer duyumlarınız hakkındaki farkındalığınızı artıracaktır. Vücut farkındalığı geliştirmek, dikkatinizi hayatınızın diğer alanlarına da konsantre olmayı ve odaklamayı öğretmenize yardımcı olacaktır. Egzersiz ayrıca bazı saldırganlıklarla iletişim kurmanın ve ifade etmenin iyi bir yoludur.')

type_9.markdown('<div style="text-align: right;">www.enneagraminstitute.com dan alınmıştır.</div>', unsafe_allow_html=True)
