
CHAT_PROMPT = '''
Write a prompt for a large language model such as GPT-4 to allow it to imitate the way a person speaks.
The prompt should be in English, keeping texts short but not missing important details.
The prompt should contain as much details as possible to allow the chatbot to duplicate the style of the given example text.
The response should include bullet points directing the LLM how to imitate the style and common phrases / words.
Don't preface the output with description or explanation, only write the bullet points as described.

Example text:
'''

TEXT_SAMPLES = '''
הנושא השני שעל סדר-היום זה ההודעה של האופוזיציה שהיא מחרימה את דיוני הוועדה. בנושא הזה אני חייב לומר: דבר ראשון, אני מבין לליבם. בכל זאת קשה לעבוד באופוזיציה. אני עבדתי כך שנה וחצי, הם עוד לא רגילים, חלקם באמת זו בשבילם הפעם הראשונה אולי באופוזיציה. וזה קשה, ויש לילות ארוכים. אני מבין, הם היו צריכים קצת ימי חופש. אז אני מבין לליבם, ואנחנו נמתין להם בסבלנות, וננהל את הדיונים בצורה מסודרת.

וכשהם יתאוששו – אולי היה קשה להם לקום מוקדם, אחרי שהם צעקו בכיכרות שלא נותנים להם לדבר. אז לכן מרוב שהם צעקו בכיכרות שלא נותנים להם לדבר, אז לא היה להם כוח לדבר איפה שבאמת מתקבלות ההכרעות כאן בכנסת. אז אני מבין לליבם, ואני מקווה שכשהם יקומו סוף סוף, אחרי שהם יפיגו את העייפות מהלילה, אולי הם יחליטו שהם כן רוצים להצטרף. אבל כמובן הדבר הזה הוא לשיקול דעתם. אבל הוא מאוד מאוד סמלי. מאוד מאוד סמלי. כשאנחנו היינו באופוזיציה הם לעגו, צעקו, על הליכוד ועל חברי כנסת מהאופוזיציה, שלא מגיעים לדיוני הוועדה. טענו שהדבר נובע מעצלות, כאשר הסיבה הייתה מאוד ברורה: הם קבעו הרכבי ועדות משפילים, שהיו הופכים את האופוזיציה לחסרת משמעות, הרבה פחות מחלקה בכנסת.

פה נתנו להם כקואליציה את החלוקה ההוגנת ביותר. אפילו מי שמשווה את מה שהם החליטו עליו בוועדת הכנסת לחלוקת הוועדות למה שאנחנו נתנו להם כעס עלינו. אני אישית כעסתי על יושב-ראש ועדת הכנסת, ואמרתי לו: למה אתה נותן להם הרבה הרבה יותר ממה שהם נתנו לנו? והוא בחר, אני מבין לליבו 
להיות באדיבות של מנצחים, ונתן הרבה יותר, ואני קיבלתי כמובן את שיקול דעתו והצבעתי בעד, כי אני חושב שיש מקום לתת לאדיבות של מנצחים. אני ממליץ לאופוזיציה לחשוב, אולי לשקול, גם על אדיבות של מפסידים, כי נראה שהם לא ממש מבינים את העניין.

כן. שנתנו באריכות לאנשים שאינם מסכימים עם עמדתי ועם עמדת חברי הקואליציה להתבטא, ולא קטענו אותם, ונתנו להם להשלים את דבריהם, והתייחסנו. כנראה שניהול דיון בצורה דמוקרטית ומכבדת זה משהו שבשמאל לא ממש מכירים, ולכן זה מפריע להם. וכשנגמרים הטיעונים, או יותר נכון כשלא מתחילים הטיעונים, הם בחרו לא לבוא. כאמור, צר לי על כך, ואני בטוח שאנחנו נבין בהמשך הדרך מה מאחורי אותה התנהלות תמוהה של האופוזיציה.

אני כבר אומר, במיוחד כאשר הלו"ז קבוע מראש: הם יודעים, והדבר נאמר כאן בוועדה, ביום ראשון הקרוב, לא הזה, המצע לדיון מונח. מסמך ההכנה מטעם הייעוץ המשפטי יונח על שולחן הוועדה.

ובהסכמתכם. אבל ההצגה לתקשורת כנראה חשובה יותר מכל דבר אחר. ואני קורא לכל אנשי האופוזיציה, וגם למומחים שהוזמנו, חלקם נמצאים פה היום: בואו, השמיעו את קולכם. אנחנו נשמע ונשקול ונדון. באמת תופעה מעניינת, כיצד אנשים כל כך חוששים מלהביע את דעתם, אולי כי הם יגלו שהציבור הישראלי יותר חכם ממה שהם חושבים שהוא.

לקחתי זמן לא רב אבל משמעותי, כדי להציג ולדבר מסביב, אבל שיהיה ברור: לא האירוע הראשון ולא האירוע השני ישפיעו לא על ההתנהלות ולא על הקצב של דיוני הוועדה. האופוזיציה תחליט שהיא חוזרת בה מהחרמה, שהיא לא חוזרת בה מהחרמה – זה עניינה. בכלל כל מי שיגיע לכאן, יקבל את מלוא הזמן ונעמוד על זכותו לדבר, מסכימים או לא מסכימים. אבל אנחנו פועלים פה בשליחות מאוד מאוד מאוד ברורה – להשיב את הריבונות לעם, ואיומים מכל כיוון שהוא אינם הדרך לנהל שיח במדינה דמוקרטית.

כמובן, חברי הוועדה שרוצים לדבר, אם אתם רוצים הצהרת פתיחה קצרה אני אתן לכם לפני. רק עכשיו, אחרי שדיברנו על המסגרת, אני אגיד בקצרה. הנוסח המוצע לדיון שנמצא בפניכם, ואני כן אבקש ממומחים שמגיעים להתייחס כמובן למה שהם רוצים בתוכו, ואם הם רוצים להתייחס לדברים מעבר לעשות זאת בצמצום, כדי שהדיון היום כן יהיה ממוקד במה שיש כאן ולא במה שאין כאן. הרבה מאוד פעמים הדיונים הולכים למקום של הייתי תומך בזה אם היה עוד דברים – זו אמירה חשובה, אבל כדאי שהיא תהיה הפרפרת למנה העיקרית, שהיא התייחסות לטיעונים לגופם. אני אבקש באמת שגם מומחים וגם חברי כנסת שרוצים לדבר שיגידו, אם הם לא מסכימים לאיזה תיקון או חושבים שצריך ללכת לכיוון אחר, שיציגו משהו אלטרנטיבי. אנחנו פתוחים ושומעים כל דבר, ולא מן השפה ולחוץ.

הנוסח לדיון עוסק בכמה סוגיות עיקריות.

נכון. אנחנו תכף נתייחס. הסוגיה הראשונה היא שינוי הרכב הוועדה לבחירת שופטים. אם תסתכלו על הנוסח, מדובר בסעיף 1 לנוסח, שמתקן את סעיף 4 לחוק-יסוד: השפיטה, שעוסק במבנה הוועדה לבחירת שופטים ומשנה את הרכבה. אני אגיד מלמעלה: ההצעה היא להשאיר את הרכב הוועדה במספר תשעה חברים, כאשר נציגי לשכת עורכי הדין יצאו מהוועדה. ותהיה לנו בעצם ועדה שמורכבת משלוש הרשויות – יהיה את נציגי הרשות השופטת, נציגי הרשות המבצעת ונציגי הרשות המחוקקת – שלושה חברי כנסת, שלושה שרים ושלושה נציגי הרשות השופטת, כאשר נציגי הרשות השופטת, מסיבות שגם עליהן נדבר, אחד מהם יהיה נשיא בית המשפט העליון, ושני האחרים יהיו נשיא בדימוס של בית משפט מחוזי ונשיא בדימוס של בית משפט שלום, שייבחרו בהסכמת הנשיא והשר. זה שינוי הרכב הוועדה.

נכון. את הווטו אנחנו מורידים, ההכרעות בוועדה אמורות להתקבל ברוב רגיל. הווטו בכל מקרה לא מופיע בחוק היסוד. החוק הזה, ואני מפנה אתכם להערת הכוכבית שמופיעה בסוף הנוסח: "התיקון יחייב עריכת תיקונים משלימים בחוק בתי המשפט [נוסח משולב]" – חלק מסדרי המינוי, סדרי העבודה של הוועדה לבחירת השופטים מופיעים בחוק בתי המשפט ולא בחוק היסוד, ולכן יהיה צריך. אנחנו כרגע עוסקים בעקרונות שבחוק היסוד, ובהתאם לדיונים פה אנחנו גם נעשה את ההתאמות בחוק בתי המשפט.

סעיף 2 מדבר על עילת הסבירות, ובעצם נוקט גישה שאומרת, אני לא רוצה להגיד בניגוד, אבל בשונה מהנוסח שהתפרסם מטעם שר המשפטים, שמדבר על עילת הסבירות ומנסה להתמודד ולבטל אותה לכל הערכאות, ולהשאיר את עילות המשפט המנהלי האחרות לכל הגופים, כאן אנחנו יותר הולכים בגישה שהציג השופט סולברג במאמריו ובפסקי דינו שאומר, שכאשר עוסקים בסבירות של נבחרי ציבור מתעוררת בעיה דמוקרטית, ולכן למקום את זה יותר בכיוון שם. כמובן אני לא יורד לפרטים, אנחנו נרד לזה בהמשך בצורה יותר מפורטת.

סעיף 3 מבטל את הביקורת השיפוטית על חוקי יסוד. הוא בעצם אומר, שבקביעת חוקי היסוד אין ביקורת שיפוטית. יש בזה גם היגיון רב, וגם אני חייב לומר שזו עמדתה העקבית של הכנסת, כאשר היא מציגה אותה בפני בית המשפט העליון, שלבית המשפט העליון אין סמכות לבטל חוקי יסוד. רק לאחרונה הוצגה עמדה ברוח זו, ואני בטוח שלכך גם יתייחסו במסמכי ההכנה, כאשר הייעוץ המשפטי יהיה ערוך לכך.

סעיף 15ב עוסק במה שמכונה מנגנון ההתגברות, והביקורת השיפוטית בעניין תוקפו של חוק. זאת אומרת, מתי בית משפט יכול לבקר חוקים בעילה של אי התאמתם לחוקי היסוד, באיזה פורום. ההצעה שלי מדברת על 15 שופטים פה אחד שיחליטו כך, כדי באמת לשמר את העיקרון שביקורת שיפוטית על תוקפו של חוק אמורה להישמר למקרים הבולטים ביותר והקיצוניים ביותר, כאשר זה לא דבר ששנוי במחלוקת. אם זה שנוי במחלוקת, סימן שזה עניין שבשיקול דעת, ואז שיקול הדעת של המחוקק אמור להיות זה שקובע בנושאי חקיקה.

אמרנו חוק יסוד קודם. סעיף 3 מדבר על שמי שבידו סמכות שפיטה לא יידרש לשאלה בדבר תוקפו של חוק-יסוד ולא יהיה תוקף להחלטה. זאת אומרת, בנושא חוק-יסוד בכלל בית המשפט לא אמור לדון בעניין תוקפו של חוק-יסוד.

אף אחד לא היה מוכן לקבל סיטואציה של בית משפט שפוסל תיקון לחוקה האמריקנית, לצורך העניין. אם מסתכלים על חוק-יסוד כעל תיקון לחוקה או משהו בעל מעמד חוקתי, לא הגיוני שבית המשפט, ששואב את סמכותו מחוק-יסוד בעצמו, יהיה זה שמושך את עצמו בציציות ראשו ואומר: אני הוקמתי מכוח חוק-יסוד: השפיטה, ואני אומר לכם: אתם לא מסוגלים לתקן חוקי יסוד.

ובכל הנוגע לחוקים רגילים, על בסיס זה שהם לא תואמים חוק-יסוד, מתוך איזושהי אמירה שחוקים רגילים אסור שיסתרו חוק-יסוד, הנושא צריך להיות, כמו שאמר חבר הכנסת סעדה, באמת רק כשזה ברור. זאת אומרת, אם הדבר שנוי במחלוקת, אז סימן שיש צדדים לכאן ולכאן, ולפחות לשיטתי אין הצדקה שנעדיף את הרוב ואת המיעוט בבית המשפט על פני הרוב והמיעוט בכנסת, אם העניין נתון בשיקול דעת.

וגם יש פה הוראה של התגברות – דהיינו התגברות או חיסון מראש, אפשר לדון גם בסוגיה הזאת כמובן – מה קורה כאשר הכנסת מראש או בדיעבד אומרת לבית המשפט: אנחנו רוצים שהחוק הזה יהיה במעמד של חוק-יסוד. אנחנו רוצים שהוא יהיה תקף על אף האמור בחוקי היסוד, ואל תתערב בו. והיא כוללת את זה בתור אמירה מפורשת בתוך החוק, ומקבלת אותו בפרוצדורה הקבועה כאן.

אכן בזמנו יצא בזמנו אפילו יצא תזכיר מטעם משרד המשפטים בסוגיית השפיטות שעוסק בנושא הזה. בזמנו הכוונה בזמן פרופ' פרידמן, כשהוא היה שר משפטים. הוא בהחלט דבר שראוי לשקול אותו. כרגע אנחנו לא שם. את לא היית בהתחלה כשאמרתי, ולהבנתי אין שום סיבה שבעולם שבמסגרת הדיון, בוודאי לא היום, אנחנו נהיה על תקן צוות התגובות של בית המשפט העליון על פסק דין דרעי. דיברתי על זה במפורש. אני חושב שפסק דין דרעי הוא פסק דין חמור מאוד, מתחתי עליו את הביקורת שראיתי לנכון, אבל הרפורמה המשפטית התחילה לפני, תימשך בלי שום קשר. אני חושב שהיא גם יכולה להשליך על מקרה דרעי, אבל הנושא של דרעי ממש איננו ביסודה, בבסיסה. יש בבסיסה עיקרון בסיסי הרבה יותר, שבו נגעת.
'''