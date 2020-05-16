cls_i_5 = ("^(НА)?[БВЛПШ]И",)

cls_iv_vow = ("ВЯ", "СТЫ")

cls_v_1_b = (
    "БЛ\+",
    "В\+",
    "ВОЗЛИ",
    "ВОПИ",
    "ЗАТ+",
    "^(ПО)?КА",
    "^ЛА",
    "ЛЕЛ\+",
    "НАД\+",
    "Р\+",
    "С\+",
    "СМ\+",
    "^ТА",
    "^ЧА",
)

cls_v_1_d = ("БЕР", "ДЕР", "ЗОВ")

cls_v_2 = ("[БП]ОР", "[КП]ОЛ", "МЕЛ")

cls_vi_1 = (
    "[БВ]Л[+Е]К",
    "[БВ]ОЛОК",
    "[БВ]ЫК",
    "Б[+Е]Г",
    "Ж[ЕЬ]?Г",
    "Л[+Е]Г",
    "Л[+Е]К",
    "МОГ",
    "НЕБР[+Е]Г",
    "НИК",
    "П[+Е]К",
    "ПРЯГ",
    "Р[+Е]Г",
    "Р[+Е]?К",
    "С[+Е]К",
    "С[+Е]К",
    "СТ[+Е]Р[+Е]Г",
    "СТРИГ",
    "Т[+Е]К",
    "ТОЛ[ОЪ]?К",
)

cls_vi_2_a = {
    "БЛЮД": "БЛЮС",
    "БР[+Е]Д": "БРЕС",
    "БР[+Е]Т": "БР+С",
    "В[+Е]Д": "ВЕС",
    "В[+Е]З": "ВЕЗ",
    "В[ЕЬ]РЗ": "ВЕРЗ",
    "ГР[+Е]Б": "ГРЕС",
    "ГРЫЗ": "ГРЫЗ",
    "ГРЯД": "ГРЯС",
    "КЛАД": "КЛАС",
    "КЛЯН": "КЛЯС",
    "КРАД": "КРАС",
    "КР[+Е]Б": "КРЕС",
    "Л[+Е]З": "ЛЕЗ",
    "МЕТ": "МЕС",
    "Н[+Е]С": "НЕС",
    "ПА[ДС]": "ПАС",
    "ПЛ[+Е]Т": "ПЛЕС",
    "ПОЛЗ": "ПОЛЗ",
    "(?<!)Р[АО]СТ?": "РАС",
    "С[+ЕИ]Д": "С+С",
    "ТРЯС": "ТРЯС",
    "ЦВ[+Е]Т": "ЦВЕС",
    "ЧТ": "ЧЕС",
}

cls_vii_1 = (
    "БЛЮ",
    "БРЕ",
    "КЛА",
    "КЛЯ",
    "КРА",
    "ПЛЕ",
    "ВЕ",
    "МЕ",
    "ПА",
    "СЕ",
    "ЧЕ",
)

cls_vii_2 = ("ДАД", "ЖИВ", "ИД", "ЫД")

cls_vii_3 = ("Д+Н", "СТАН")

cls_viii = ("ДА", "СОЗДА", ".+ЗНА", ".+СТА")

cls_x_e = (
    "БД",
    "БЛЕСТ",
    "БОЛ",
    "ВЕЛ",
    "ВЕРТ",
    "ВИД",
    "ВИС",
    "ГОР",
    "ГРЕМ",
    "ГУД",
    "ЗАВИС",
    "ЗВЕН",
    "ЗР",
    "КИП",
    "КИШ",
    "КОПТ",
    "ЛЕТ",
    "НЕНАВИД",
    "ОБИД",
    "ПЫХТ",
    "СВИСТ",
    "С[+ЕИ]Д",
    "СИП",
    "СКОРБ",
    "СКРИП",
    "СМЕРД",
    "СМОТР",
    "ТЕРП",
    "ХОТ",
    "ХРАП",
    "ХРИП",
    "ХРУСТ",
    "ШЕЛЕСТ",
    "ШИП",
    "ШУМ",
)

cls_x_a = (
    "БО",
    "ВИЗЖ",
    "ВОРЧ",
    "ДЕРЖ",
    "ДР[ЕЯ]БЕ[ЗЖ]Ж",
    "ДРОЖ",
    "ДЫШ",
    "ЖУЖЖ?",
    "ЖУРЧ",
    "ЗВУЧ",
    "КРИЧ",
    "Л[+Е]Ж",
    "МОЛЧ",
    "МЧ",
    "МЫЧ",
    "ПИЩ",
    "РЫЧ",
    "СЛЫШ",
    "СТО",
    "СТУЧ",
    "ТОРЧ",
    "ТР[+Е]Щ",
    "ШУРШ",
)

cls_x_i = (
    "БЛАГОДАР",
    "ВЕСЕЛ",
    "ВОД",
    "ВХОД",
    "ЛЮБ",
    "МН",
    "МОЛ",
    "МУЧ",
    "МЫСЛ",
    "НОС",
    "ХОД",
    "ПАСТ[ЪЬ]?В",
    "ПЛАТ",
    "ПОДОБ",
    "ПОНОС",
    "^(НА)?ПО",
    "ПРАВ",
    "ПРОС",
    "РАС",
    "СВ[+Е]ТЛ?",
    "СЛАВ",
    "СЛУЖ",
    "СТРАШ",
    "ТВОР",
    "ТОМ",
    "ТОЧ",
    "УЧ",
    "ХВАЛ",
    "ХРАН",
)

jotted_zh = (
    "^[+Е]ЗД",
    "Б[+Е]Д",
    "БЛИЗ",
    "БОРОЗД",
    "БУД",
    "ВАД",
    "ВОД",
    "ВОЗ",
    "Г(РА|ОРО)Д",
    "ГАД",
    "ГВОЗД",
    "ГРОМОЗД",
    "КАЗ",
    "(?<!Б)ЛАД",
    "М(ЛА|ОЛО)Д",
    "М(РА|ОРО)З",
    "НИЗ",
    "НУД",
    "ОБИД",
    "ПЛОД",
    "ПРУД",
    "Р[+Е]Д",
    "РАЗ",
    "РОД",
    "РЯД",
    "С[+Е]РД",
    "С[+ЕИ]Д",
    "САД",
    "СВОБОД",
    "СЛ[+Е]Д",
    "СНАБД",
    "СТРАД",
    "СТУД",
    "СТЫД",
    "СУД",
    "ТВ[+Е]РД",
    "^УД",
    "^УЗ",
    "Х(ЛА|ОЛО)Д",
    "ХОД",
    "Ц[+Е]Д",
    "ЧУД",
    "ЩАД",
)

jotted_sch = (
    "Б[+Е]С",
    "В[+Е]С",
    "ВЫС",
    "Г(ЛА|ОЛО)С",
    "ГАС",
    "КВАС",
    "КОС",
    "КР[+Е]С",
    "КРАС",
    "КУС",
    "М[+Е]С",
    "НОС",
    "ПИС",
    "РОС",
    "ТРУС",
)

jotted_tsch = (
    "[БВ](РА|ОРО)Т",
    "Б(ЛА|ОЛО)Т",
    "БОГАТ",
    "В(РА|ОРО)Т",
    "В[+Е]РТ",
    "В[+Е]СТ",
    "ВСТР[+Е]Т",
    "ГЛОТ",
    "ГОСТ",
    "ГУСТ",
    "З(ЛА|ОЛО)Т",
    "ЗАБОТ",
    "ИСК",
    "К(ЛА|ОЛО)Т",
    "К(РА|ОРО)Т",
    "К(РА|ОРО)Т",
    "КАТ",
    "КОПТ",
    "КОСТ",
    "КР[+Е]СТ",
    "КРОТ",
    "КРУТ",
    "(?<!В)Л[ЕЬ]СТ",
    "ЛОПАТ",
    "ЛОХМАТ",
    "М(ЛА|ОЛО)Т",
    "М[+Е]СТ",
    "М[+Е]Т",
    "МОСТ",
    "МСТ",
    ".+МУТ",
    "ПЛАТ",
    "ПЛОТ",
    "ПОРТ",
    "ПОСТ",
    "ПР[+Е]Т",
    "ПРОСТ",
    "ПУСТ",
    "ПЯТ",
    "РАБОТ",
    "(?<!М)РАСТ",
    "С[+Е]Т",
    "СВ[+Е]Т",
    "СВЯТ",
    "СЛАСТ",
    "СМ[+Е]РТ",
    "СНАСТ",
    "СЫТ",
    "ТРАТ",
    "ТЯГОТ",
    "ХВАТ",
    "ХИТ",
    "ХОТ",
    "ЦВ[+Е]Т",
    "Ч[+Е]РТ",
    "Ч[+Е]СТ",
    "ЧАСТ",
    "ЧИСТ",
    "ЩИТ",
    "ЩУТ",
)

isol = {
    "В\+ДИ": "В+ДА",
    "В\+ЖД": "В+ДА",
    "ВИЖД": "ВИД+",
    "ДАДИ": "ДА",
    "ДАЖД": "ДА",
    "БУД": "БЫ",
    "В\+Д": "В+ДА",
    "В\+С": "В+ДА",
    "ДАД": "ДА",
    "ДАС": "ДА",
    "ДАТ": "ДА",
    "ИМА": "ИМА",
    "Н\+С": "БЫ",
    "ЯДИ": "ЯС",
    "ЯЖД": "ЯС",
    "В\+": "В+ДА",
    "ДА": "ДА",
    "ЕС": "БЫ",
    "ИМ": "ИМА",
    "ЯД": "ЯС",
    "ЯС": "ЯС",
    "^Е": "БЫ",
    "^С": "БЫ",
    "^Я": "ЯС",
}
