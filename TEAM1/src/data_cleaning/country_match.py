
# Matches municipality code for city/country (post 2010 data) to municipality code for country
# Key is code for municipality in post-2010 data
# Value is a 2-tuple containing (<code for country in pre-2010 data>, <Name of Country in pre-2010 data>)
country_code_map = {

    #Maps code for ABIDJAN-COTE/Abidija (Abidjan Cote de'Ivoire)
    29254 : (98582, "COSTA DO MARFIM"), 

    #Maps code for ABU DHABI-EAU/Abu Dhabi (Abu Dhabi, UAE)
    29262 : (98728, "EMIRADOS ARABES"),

    #Maps code for ACCRA, Ghana
    29270 : (98043, "GANA"),

    #Maps code for AMÃ-JORD (Amman, Jordan)
    29289 : (29181, "JORDANIA"),

    #Maps code for ANCARA-TURQ/ANCARA (Ankara, Turkey)
    29297 : (98108, "TURQUIA"),

    #Maps code for ARGEL-ARGL/ARGEL (Algiers, Algeria)
    29300 : (98701, "ARGELIA"),

    #Maps code for  ARTIGAS (Uruguay)
    29319 : (11568, "URUGUAI"),

    #Maps code for ASSUNÇÃO-PARG (Asuncion, Paraguay)
    29327 : (11444, "PARAGUAI"),

    #Maps code for ATENAS-GREC (Athens, Greece)
    29335 : (11827, "GRECIA"),

    #Maps code for ATLANTA-EUA (Atlanta, USA)
    39080 : (11266, "ESTADOS UNIDOS"),

    #Maps code for BANGKOK-TAIL (Bangkok, Thailand)
    29343 : (98205, "TAILANDIA"),

    #Maps code for BARCELONA-ESPA (Barcelona, Spain)
    29351 : (11240, "ESPANHA"),

    #Maps code for  BEIRUTE-LBAN (Beirut, Lebanon)
    29360 : (11401, "LIBANO"),

    #Maps code for  BERLIM-RFA (Berlin, Germany)
    29386 : (11100, "ALEMANHA"),

    #Maps code for  BISSAU-GUIB (Guinea-Bissau)
    29394 : (98027, "GUINE BISSAU"),

    #Maps code for  BOGOTÁ-COLO (Bogota, Colombia)
    29408 : (11185, "COLOMBIA"),

    #Maps code for  BOSTON-EUA (Boston, USA)
    29416 : (11266, "ESTADOS UNIDOS"),

    #Maps code for  BRIDGETOWN (Bridgetown, Barbados)
    29424 : (98663, "BARBADOS"),

    #Maps code for BRUXELAS (Brussels, Belgium)
    29432 : (98922, "BELGICA"),

    #Maps code for BUCARESTE (Bucarest, Romania)
    29440 : (98647, "ROMENIA"),

    #Maps code for BUDAPESTE (Budapest, Hungary)
    29459 : (29238, "HUNGRIA"),

    #Maps code for BUENOS AIRES (Buenos Aires, Argentina)
    29467 : (11142, "ARGENTINA"),

    #Maps code for CORDOBA (Cordoba, Argentina)
    29602 : (11142, "ARGENTINA"),

    #Maps code for CAIENA (Cayenne, French Guiana)
    29475 : (11320, "GUIANA FRANCESA"),

    #Maps code for CAIRO (Cairo, Egypt)
    29483 : (98086, "EGITO"),

    #Maps code for CAMBERRA (Canberra, Australia)
    29491 : (98981, "AUSTRALIA"),

    #Maps code for CANTAO (Guangzhou, China)
    30651 : (98540, "CHINA"),

    #Maps code for CARACAS (Caracas, Venezuela)
    29505 : (11584, "VENEZUELA"),

    #Maps code for CHICAGO (Chicago, USA)
    29513 : (11266, "ESTADOS UNIDOS"),

    #Maps code for CHUY (Chuy, Uruguay)
    29521 : (11568, "URUGUAI"),

    #Maps code for CIDADE DO CABO (Cape Town, South Africa)
    29530 : (98787, "AFRICA DO SUL"),

    #Maps code for CIUDAD DEL ESTE (Ciudad del Este, Paraguay)
    29556 : (11444, "PARAGUAI"),

    #Maps code for CIUDAD GUAYANA (Ciudad Guayana, Venezuela)
    29564 : (11584, "VENEZUELA"),

    #Maps code for COCHABAMBA (Cochabamba, Bolivia)
    29572 : (11800, "BOLIVIA"),

    #Maps code for CONCEPCION (Concepcion, Paraguay)
    29580 : (11444, "PARAGUAI"),

    #Maps code for COPENHAGUE-DINA (Copehhagen, Denmark)
    29599 : (98485, "DINAMARCA"),

    #Maps code for DACAR (Dakar, Senegal)
    29610 : (98248, "SENEGAL"),

    #Maps code for DAMASCO (Damascus, Syria)
    29637 : (98221, "SIRIA"),

    #Maps code for DUBLIN (Dublin, Ireland)
    29661 : (29033, "IRLANDA"),

    #Maps code for ENCARNACION (Encarnacion, Paraguay)
    29670 : (11444, "PARAGUAI"),

    #Maps code for ESTOCOLMO (Stockholm, Sweden)
    29688 : (98744, "SUECIA"),

    #Maps code for FARO (Faro, Portugual)
    30961 : (11509, "PORTUGAL"),

    #Maps code for FRANKFURT (Frankfurt, Germany)
    29696 : (11100, "ALEMANHA"),

    #Maps code for GENEBRA (Geneva, Switzerland)
    29700 : (11525, "SUICA"),

    #Maps code for GEORGETOWN (Georgetown, GUYANA)
    29718 : (11304, "GUIANA"),

    #Maps code for GUATEMALA (Guatemala) - No-op
    98000 : (98000, "GUATEMALA"),

    #Maps code for HAMMATSU (Hammatsu, Japan)
    29742 : (11380, "JAPAO"),

    #Maps code for HANOI (Hanoi, Vietnam)
    29750 : (2800, "VIETNA"),

    #Maps code for HARARE (Harare, Zimbabwe)
    29769 : (29092, "ZIMBABWE"),

    #Maps code for HARTFORD (Hartford, CT, USA)
    30902 : (11266, "ESTADOS UNIDOS"),

    #Maps code for HAVANA (Havana, Cuba)
    29777 : (98868, "CUBA"),

    #Maps code for HELSINQUE (Helsinki, Finland)
    29785 : (98426, "FINLANDIA"),

    #Maps code for HONG KONG-HONG (Hong Kong)
    29793 : (29025, "HONG KONG"),

    #Maps code for HOUSTON (Houston, TX, USA)
    29807 : (11266, "ESTADOS UNIDOS"),

    #Maps code for IAUNDE (Yaounde, Cameroon)
    29815 : (29220, "REPUBLICA DOS CAMAROES"),

    #Maps code for IQUITOS (Iquitos, Peru)
    29823 : (11460, "PERU"),

    #Maps code for ISLAMABADE (Islamabad, Pakistan)
    29831 : (98302, "PAQUISTAO"),

    #Maps code for ISTAMBUL (Istanbul, Turkey)
    39306 : (98108, "TURQUIA"),

    #Maps code for JACARTA (Jakarta, Indonesia)
    29840 : (29211, "INDONESIA"),

    #Maps code for KIEV (Kiev, Ukraine)
    29858 : (11762, "UCRANIA"),

    #Maps code for KINGSTON-JAMAICA (Kingston, Jamaica)
    99430 : (29190, "JAMAICA"),

    #Maps code for KUAITE (Kuwait)
    29882 : (29157, "KUWAIT"),

    #Maps code for KUALA LUMPUR (Kuala Lumpur, Malaysia)
    29890 : (29130, "MALASIA"),

    #Maps code for LA PAZ (La Paz, Bolivia)
    29904 : (11800, "BOLIVIA"),

    #Maps code for LAGOS (Lagos, Nigeria)
    29912 : (98361, "NIGERIA"),

    #Maps code for LETHEM (Lethem, Guiana)
    99422 : (11304, "GUIANA"),

    #Maps code for LIBREVILLE (Libreville, Gabon)
    29939 : (98060, "GABAO"),

    #Maps code for LIMA (Lima, Peru)
    29947 : (11460, "PERU"),

    #Maps code for Lisboa (Lisbon, Portugal)
    29955 : (11509, "PORTUGAL"),

    #Maps code for LOME (Lome, Togo)
    29963 : (98167, "TOGO"),

    #Maps code for LONDRES (London, UK)
    29971 : (98841, "INGLATERRA"),

    #Maps code for LOS ANGELES (Los Angeles, USA)
    29980 : (11266, "ESTADOS UNIDOS"),

    #Maps code for LUANDA (Luanda, Angola)
    29998 : (98965, "ANGOLA"),

    #Maps code for MEXICO, MEXICO (Mexico City, Mexico)
    30104 : (11428, "MEXICO"),

    #Maps code for MADRI (Madrid, Spain)
    30066 : (11240, "ESPANHA"),

    #Maps code for MANAGUA (Managua, Nicaragua)
    30074 : (98838, "NICARAGUA"),

    #Maps code for MANILA (Manila, Phillippines)
    30082 : (98442, "FILIPINAS"),

    #Maps code for MAPUTO (Maputo, Mozambique)
    30090 : (29116, "MOCAMBIQUE"),

    #Maps code for MENDOZA (Mendoza, Argentina)
    39004 : (11142, "ARGENTINA"),

    #Maps code for MIAMI (Miami, USA)
    30112 : (11266, "ESTADOS UNIDOS"),

    #Maps code for MILAO (Milan, Italy)
    30120 : (11363, "ITALIA"),

    #Maps code for MONTEVIDEO (Montevideo, Uruguay)
    30147 : (11568, "URUGUAI"),

    #Maps code for MONTREAL (Montreal, Canada)
    30155 : (98906, "CANADA"),

    #Maps code for MOSCOU (Moscow, Russia)
    30163 : (98760, "RUSSIA"),

    #Maps code for MUMBAI (Mumbai, India)
    30171 : (98825, "INDIA"),

    #Maps code for MUNIQUE (Munich, Germany)
    30180 : (11100, "ALEMANHA"),

    #Maps code for NAGOIA (Nagoya, Japan)
    30198 : (11380, "JAPAO"),

    #Maps code for NAIROBI (Nairobi, Kenya)
    30201 : (29165, "KENIA"),

    #Maps code for NOVA DELHI (New Delhi, India)
    30210 : (98825, "INDIA"),

    #Maps code for NOVA YORK (New York, USA)
    30228 : (11266, "ESTADOS UNIDOS"),

    #Maps code for OSLO (Oslo, Norway)
    30244 : (98345, "NORUEGA"),

    #Maps code for OTTAWA (Ottawa, Canada)
    30252 : (98906, "CANADA"),

    #Maps code for PANAMA-PAN (Panama City, Panama)
    30260 : (98329, "PANAMA"),

    #Maps code for PARAMARIBO (Paramaribo, Suriname)
    30279 : (11541, "SURINAME"),

    #Maps code for PARIS (Paris, France)
    30287 : (11282, "FRANCA"),

    #Maps code for PASO LOS LIBRES (Paso de los Libres, Argentina)
    30295 : (11142, "ARGENTINA"),

    #Maps code for PEDRO JUAN CABALLERO (Pedro Juan Caballero, Paraguay)
    30309 : (11444, "PARAGUAI"),

    #Maps code for PEQUIM (Beijing, China)
    30317 : (98540, "CHINA"),

    #Maps code for PORT OF SPAIN (Port of Spain, Trinidada and Tobago)
    30325 : (98140, "TRINIDAD TOBAGO"),

    #Maps code for PORTO (Porto, Portugal)
    30341 : (11509, "PORTUGAL"),

    #Maps code for PORTO PRINCIPE (Port-au-Prince , Haiti)
    30333 : (29246, "HAITI"),

    #Maps code for PRAIA (Praia , Cape Verde)
    30368 : (98604, "CABO VERDE"),

    #Maps code for PRETORIA (Pretoria, South Africa)
    30376 : (98787, "AFRICA DO SUL"),

    #Maps code for PUERTO IGUAZU (Puerto Iguazu, Argentina)
    99155 : (11142, "ARGENTINA"),

    #Maps code for PUERTO QUIJARRO (Puerto Quijarro, Bolivia)
    99236 : (11800, "BOLIVIA"),

    #Maps code for QUITO (Quito, Ecuador)
    30392 : (11223, "EQUADOR"),

    #Maps code for RABAT (Rabat, Morroco)
    30406 : (29122, "MARROCOS"),

    #Maps code for RIADE (Riyadh, Saudi Arabia)
    30422 : (11126, "ARABIA SAUDITA"),

    #Maps code for RIO BRANCO (Rio Branco, Uruguay)
    30430 : (11568, "URUGUAI"),

    #Maps code for ROMA (Rome, Italy)
    30449 : (11363, "ITALIA"),

    #Maps code for ROTTERDAO (Rotterdam, Netherlands)
    30457 : (29009, "PAISES BAIXOS"),

    #Maps code for SAO DOMINGOS (Santo Domingo, Dominican Republic)  
    30490 : (98280, "REPUBLICA DOMINICANA"),

    #Maps code for SAO FRANCISCO (San Francisco, USA) 
    30503 : (11266, "ESTADOS UNIDOS"),

    #Maps code for SAO JOSE (San Jose, Costa Rica) 
    30511 : (98507, "COSTA RICA"),

    #Maps code for SAO SALVADOR (San Salvador, El Salvador) 
    30520 : (98469, "EL SALVADOR"),

    #Maps code for SOFIA (Sofia, Bulgaria) 
    30546 : (98620, "BULGARIA"),

    #Maps code for SALTO DE GUAIRA (Salto del Guaira, Paraguay)
    30465 : (11444, "PARAGUAI"),

    #Maps code for SANTIAGO (Santiago, Chile)
    30481 : (11169, "CHILE"),

    #Maps code for SEUL (Seoul, South Korea)
    30538 : (11207, "COREIA"),

    #Maps code for SINGAPURA-SING (Singapore)
    29548 : (98523, "CINGAPURA"),

    #Maps code for SSTA C LA SIERRA-BOLI (Santa Cruz de la Sierra, Bolivia)
    30473 : (11800, "BOLIVIA"),

    #Maps code for SYDNEY (Sydney, Australia)
    30562 : (98981, "AUSTRALIA"),

    #Maps code for TOQUIO (Tokyo, Japan)
    30627 : (11380, "JAPAO"),

    #Maps code for TAIPEI (Taipei, Taiwan)
    30570 : (2828, "TAIWAN"),

    #Maps code for TEERA (Tehran, Iran)
    30597 : (29203, "IRA"),

    #Maps code for TEGUCIGALPA (Tegucigalpa, Honduras)
    30600 : (29076, "HONDURAS"),

    #Maps code for TEL AVIV (Tel Aviv, Israel)
    30619 : (11347, "ISRAEL"),

    #Maps code for TORONTO (Toronto, Canada)
    30635 : (98906, "CANADA"),

    #Maps code for TRIPOLI (Tripoli, Libya)
    30686 : (29149, "LIBIA"),

    #Maps code for TUNIS (Tunis, Tunisia)
    30708 : (98124, "TUNISIA"),

    #Maps code for VANCOUVER (Vancouver, Canada)
    39063 : (98906, "CANADA"),

    #Maps code for VARSOVIA (Warsaw, Poland)
    30740 : (11487, "POLONIA"),

    #Maps code for VIENA (Vienna, Austria)
    30767 : (98949, "AUSTRIA"),

    #Maps code for WASHINGTON (Washington DC, USA)
    30783 : (11266, "ESTADOS UNIDOS"),

    #Maps code for WELLINGTON (Wellington, New Zealand)
    30805 : (29050, "NOVA ZELANDIA"),

    #Maps code for WINDHOEK (Windhoek, Namibia)
    30821 : (29068, "NAMIBIA"),

    #Maps code for XANGAI (Shanghai, China)
    30848 : (98540, "CHINA"),

    #Maps code for ZURIQUE (Zurich, Switzerland)
    30864 : (11525, "SUICA"),

    #Maps code for MITSUKAIDO-JAPA (Mitsukaido, Japan)
    30139 : (11380, "JAPAO"),

    #Maps code for SUZUKA-JAPA (Suzuka, Japan)
    30554 : (11380, "JAPAO"),

    #Maps code for TAKAOKA-JAPA (Takaoka, Japan)
    30589 : (11380, "JAPAO"),

    #Maps code for TOYOHASHI-JAPA (Toyohashi, Japan)
    30643 : (11380, "JAPAO"),

    #Maps code for UEDA-JAPA (Ueda, Japan)
    30724 : (11380, "JAPAO"),

    #Maps code for OIZUMI-JAPA (Oizumi, Japan)
    30236 : (11380, "JAPAO"),

    #Maps code for GUATEMALA-GUAT (Guatemalteca, Japan)
    29726 : (98000, "GUATEMALA"),

    #Maps code for KINGSTON-JAMA (Kingston, Jamaica)
    29866 : (29190, "JAMAICA"),

    #Maps code for DONGGUAN-CHIN (Donguan, China)
    30880 : (98540, "CHINA"),

    #Maps code for PUERTO SUAREZ-BOL (Puerto Suarez, Bolivia)
    30384 : (11800, "BOLIVIA"),


    #-----------------------------------------------#
    # Mappings for Countries not in pre-2010 Data
    #-----------------------------------------------#

    #Maps code for  BELGRADO-SERV (Belgrade, Serbia)
    #Note: this would have been included in IUGUSLÁVIA (code 29173), so left region code and updated country
    29378 : (29378, "SERVIA"),

    #Maps code for FREETOWN (Freetown, Sierra Leone)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    99406 : (99406, "SERRA LEOA"),

    #Maps code for ASTANA-KAZA (Astana, Kazakhstan)
    #Note: there is no prior country code for kazakhstan, so left region code and updated country
    39241 : (39241, "CAZAQUISTAO"),

    #Maps code for GABORONE (Gaborone, Botswana)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    30669 : (30669, "BOTSWANA"),

    #Maps code for  BRATISLAVA (Bratislava, Slovakia)
    #Note, in pre-2010 datasets, this is part of Czechoslovakia, so left region code and updated country
    39209 : (39209, "ESLOVAKIA"),

    #Maps code for COLOMBO (Colombo, Sri Lanka)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    30929 : (30929, "SRI LANKA"),

    #Maps code for CONACRI (Conakry, Guinea)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    38903 : (38903, "GUINE"),

    #Maps code for COTONOU (Cotonou, Benin)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    38920 : (38920, "BENIM"),
    
    #Maps code for DAR ES SALAAM (Dar ese Salaam, Tanzania)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    38962 : (38962, "TANZANIA"),

    #Maps code for DOHA (Doha, Qatar)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    29653 : (29653, "CATAR"),

    #Maps code for DILI (Dili, Timor-Leste)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    29645 : (29645, "TIMOR-LESTE"),

    #Maps code for IEREVAN-ARME (Yereven, Armenia)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    38989 : (38989, "ARMENIA"),

    #Maps code for  BRAZZAVILLE (Brazzaville, Republic of Congo)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    #Note Republic of Congo != Democratic Republic of Congo
    39187 : (39187, "REPUBLICA DO CONGO"),

    #Maps code for KINSHASA (Kinshasa, Democratic Republic of the Congo)
    #Note Democratic Republic of Congo != Republic of Congo
    29874 : (29874, "REPUBLICA DEMOCRATICA DO CONGO"),

    #Maps code for LILONGUE (Lilongwe, Malawi)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    99341 : (99341, "MALAWI"),

    #Maps code for LIUBLIANA (Ljubljana, Slovenia)
    39160 : (39160, "ESLOVENIA"),

    #Maps code for LUSACA (Lusaca, Zambia)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    99287 : (99287, "ZAMBIA"),

    #Maps code for MASCATE (Muscat, Oman)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    39102 : (39102, "OMA"),

    #Maps code for NASSAU (Nassau, Bahamas)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    99180 : (99180, "COMUNIDADE DAS BAHAMAS"),

    #Maps code for NICOSIA (Nicosia, Cyprus)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    39322 : (39322, "CHIPRE"),

    #Maps code for PRAGA (Prague, Czech Replublic)
    #Note, in pre-2010 datasets, this entry does not exist (was part of Czechoslovakia - 98566), so left region code and updated country
    30350 : (30350, "REPUBLICA CHECA"),

    #Maps code for RAMALLAH-PALE (Ramallah, Palestine)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    30414 : (30414, "PALESTINA"),

    #Maps code for SAO TOME (Sao Tome, Sao Tome and Principe) 
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    39225 : (39225, "SAO TOME E PRINCIPE"),

    #Maps code for SARAJEVO (Sarajevo, Bosnia and Herzegovina) 
    #Note, in pre-2010 datasets, this entry does not exist (part of Yugoslavia - code 29173), so left region code and updated country
    30988 : (30988, "BOSNIA E HERZEGOVINA"),

    #Maps code for TALIN (Talinn, Estonia)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    99317 : (99317, "ESTONIA"),

    #Maps code for TBILISI (Tbilisi, Georgia)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    99104 : (99104, "GEORGIA"),

    #Maps code for UAGADUGU (Ouagadougou, Burkina Faso)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    39284 : (39284, "BURQUINA FASSO"),
    
    #Maps code for YANGON (Yangon, Myanmar)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    99376 : (99376, "MYANMAR"),
    
    #Maps code for ZAGREB (Zagreb, Croatia)
    #Note, in pre-2010 datasets, this entry does not exist (part of Yugoslavia - code 29173), so left region code and updated country
    39020 : (39020, "CROACIA"),

    #Maps code for BELMOPAN-BELI (Belmopan, Belize)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    38881 : (38881, "BELIZE"),

    #Maps code for MALABO-GNEQ (Malabo, Equatorial Guinea)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    39263 : (39263, "GUINE EQUATORIAL"),

    #Maps code for BAMAKO (Bamako, Mali)
    #Note, in pre-2010 datasets, this entry does not exist, so left region code and updated country
    99350 : (99350, "MALI"),
    
    
    #-----------------------------------------------#
    #Non-standard Country Mappings
    #-----------------------------------------------#

    #Maps code for KATMANDU (Kathmandu, Nepal)
    #Note, in pre-2010 datasets, this entry does not exist. I've updated the country,
    #but the region code (29173) is used in earlier datasets for Yugoslavia. I've reset the code
    #to 0 to eliminate collisions
    29173 : (0, "NEPAL"),


    #-----------------------------------------------#
    # Country to Country Mappings
    #-----------------------------------------------#

    #Maps code for  ARGENTINA (Argentina)
    11142 : (11142, "ARGENTINA"),

    #Maps code for  URUGUAI (Uruguay)
    11568 : (11568, "URUGUAI"),

    #Maps code for  CHINA (China)
    98540 : (98540, "CHINA"),

    #Maps code for  ZIMBABWE (Zimbabwe)
    29092 : (29092, "ZIMBABWE"),

    #Maps code for  BOLIVIA (Bolivia)
    11800 : (11800, "BOLIVIA"),

    #Maps code for  NIGERIA (Nigeria)
    98361 : (98361, "NIGERIA"),
    
    #Maps code for  GANA (Ghana)
    98043 : (98043, "GANA"),

    #Maps code for  HAITI (Haiti)
    29246 : (29246, "HAITI"),

    #Maps code for  PAQUISTAO (Pakistan)
    98302 : (98302, "PAQUISTAO"),

    #Maps code for  PERU (Peru)
    11460 : (11460, "PERU"),

    #Maps code for  UCRANIA (Ukraine)
    11762 : (11762, "UCRANIA"),

    #Maps code for  ZIMBABWE (Zimbabwe)
    29092 : (29092, "ZIMBABWE"),

}




