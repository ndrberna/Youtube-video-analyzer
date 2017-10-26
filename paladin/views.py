from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from django.shortcuts import render_to_response, render, redirect
from django.template.context import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from time import sleep
from PIL import Image

import blockspring
import json

from .models import Query, Result

# Don Matteo test id list 
# ["2QB-PaW3kOM ","laU91jGJn-g ","w-q0WJOTOYI ","_isH35afpDc ","dxVrJ4Oy-3k ","u79Ch3oPzgs ","wqMWA_4oRlE ","9UdKsSENjmM ","R2rxZ5d5PAQ ","qXW8FaZb1S8 ","Er1dfEZNHPU ","XgBXSsPspbc ","iRMfBAiHrhE ","CkZLGfpCnBE ","SWS5HNQAuwI ","lP0orzEZY8Q ","YbZ8kK79CVw ","vPE9w_r7eQk ","9-33hI_Esvw ","52HFeKrb8Zs ","rbRprIwsoGg ","L909KE1PnwA ","qItlmYycy7k ","HuiSH2J-vgM ","M6H-6Nd3GF0 ","NY0ec7HuOo4 ","rbRprIwsoGg ","XzKtLu35MU4 ","eQ7NdkFWtak ","bj9LFwVKC_o ","52HFeKrb8Zs ","XIskSh5_XKQ ","H78OpRKp2zo ","lP0orzEZY8Q ","zQfOH3lE9hE ","DZoFJH7bwJU ","XRpkIiJ4OYw ","OwcYDVL6NV4 ","qItlmYycy7k ","L909KE1PnwA ","HuiSH2J-vgM ","N-qRwFv2O70 ","qxymETaPl7k ","uc04UKzUrhY ","dJA0aYGeeWw ","AdiDpvfQIbM ","gYIzQPdAa7M ","YLV_7VwfCXE ","3QQQaCvyV6g ","nJOOYjrKyI4 ","w6o9bbYfjD0 ","75kQrsEA1qk ","-lyE_hzudac ","UBaDUjpMtts ","6wXOBhcpw-o ","arFhG7AQzTw ","GTDsB3vqAq0 ","GbG82C0PUkI ","_R85h8BIpg4 ","Ce6rYO7p42E ","fKsPulxnmak ","ESjFlM50EPs ","JDiAsPKaYcE ","S1_Mfb6VQ6o ","ttr2M-HmPig ","pXStqDfsKu0 ","CyVWoqONw9s ","ekGdvF3t64M ","mekTfjy_EE4 ","j0PsWqsNkOo ","HqFmTQbRluo ","2P9QfVN4XMc ","UVFkoYZfZ_U ","ItbmOOXo6nM ","eJ3WyGyX5YU ","DbaTAeLPRdM ","JtM5KL7FMkI ","LwNOsWteUIU ","SrN2NML2mJY ","QBE7M2I1Osw ","6MevhHOMrzM ","1xDFFUJHfJg ","vBCI6lG_4F8 ","idA0fYsV8No ","m9aigVWvpJs ","gxwrTiIefJg ","j0PsWqsNkOo ","_JjGmDIMlLo ","jnEWDl1qmgQ ","RGFjS8Lq2uQ ","xDZt2MJLq0A ","4MZ2rTe2jSs ","KEt0usf9Euw ","b1GTFqRuDvs ","Znl4geK4vEw ","7sAe1_PrzI8 ","GKIPt6eYRPk ","3Y5aBCAUeI8 ","4FLkf5sHfi4 ","3qOjEkkaqM0 ","-_z9UfUxTFs ","O5Z12aY4e08 ","18qp9FxB_Gw ","DMgaVctGhYI ","0shA25jYhIs ","_ce4SlYRDgo ","-k_NluhyEMQ ","mLu4V5aDV9I ","0_M2c-FW6WI ","MCVSI6CPqpE ","rDtmsU1-0H8 ","45uuJAV7Qgg ","pqycKAlS87U ","lZ9GiJGdPug ","Oqg4sqH2FM4 ","U1G3IM8hf0s ","Rugbqt--1cw ","SlCsLnX9fjo ","CHPxL4xCznw ","uGqoyzv6nMs ","i4kO7m52JPs ","23L5h0YHpd8 ","Fwsa9HX2qZU ","7TSXL17Xh1M ","5TY_qVW1QFA ","gfG9h8DL7oc ","-MdHZNfISDY ","FyfeD3zqUW8 ","uYENolTHy_M ","TCetoHsCLgk ","pFbdlXMax8c ","yj8aM8QaCDM ","HdntYoIvZeQ ","dmiFK2wyr8Y ","YMg1ismdvYE ","1QeWpEBg9wM ","GRMAtAv4Qy0 ","aEFaFc48x-s ","rFPqmwGD1C0 ","S17U42UJ9DE ","tJoNlmIvfRc ","Egqwu52RGD0 ","1sx7ky624Ms ","FDhHjcoybAw ","SCWQTbuHRtI ","VkePfB5Iguw ","-xaf2IqwKEs ","YrMqrzlGAss ","DxaP9W6r9FY ","XUcYcbB3k5Q ","zSrxAu8Euzs ","H_FCcVDihks ","Onc5ngc3978 ","Kf5kIiWKDmw ","dL3F71A4_sA ","FNMHWlfVMp4 ","olNf9dgpJ-Q ","ZTQj6S3pTs4 ","KxBGmt2MTQY ","3DpIOE2DEi0 ","cT2wCjNwYm0 ","P57KKV3lRzU ","e3MPD-S7B-A ","qbl1mJpqbhQ ","ch1scTH3XKM ","PgnNBtzvrAw ","aeakTsX0tvM ","TJVniVlUXig ","dMvztClTIjo ","ffB_GCRko_I ","ZoJHYz4Ab4w ","4qEBOwwseQ8 ","E4c7ZMXfqPk ","-8zrd1xk09k ","TzaH6-3nJvk ","_dmqJOIrRVA ","LJ82unGaUo4 ","uHoAH7kvPfE ","fElUIEZ5f5E ","AaYsS_fQIms ","4BPWYd1cqpY ","aOjhYNevsCI ","SRmvjvO-6iE ","K38tMOFP9pc ","ELyXSHi_dxo ","hG8RJ3mqmOM ","4RbQ9ZZ5olY ","p-pu18BB_O0 ","yNo03NW2KSU ","7Nvp53WLa6M ","xgWAem967Lw ","vqR6P4Z79A0 ","_WvACFORTB4 ","gb5kvjk-VK4 ","2cP5cTLPn34 ","wO2TJG18I4U ","5XH3DHQ9mQE ","3UU-3jYqCFU ","pbNwzWVIywE ","uwH1XCrFKuU ","pi4T1Mkktjs ","MBcY6QiD1yM ","F9oc9gGV-vg ","g3mfAfpGYqM ","IIZ-9uReiIA ","dmA5lX9-aEE ","ILi8nYBulAE ","jhleuK_Ep2w ","wDIeZG7vlGk ","uTxEGVFT0mk ","PmYb_hjjXng ","p5sle_SYC-w ","v5-3kJKk3w8 ","_BsoSCHU1Lw ","hkpNyL27ajE ","5KYinte7Ykc ","KIDiZa-qTi0 ","hZTT-O27GiA ","CQ5HRA5I6jc ","faviW0_nAaM ","w8f2aftLQWk ","VuPcsmwxwV0 ","SGevGYfzlW0 ","LptOWuMZdZQ ","eA1K7OpQf44 ","JLT5i2qf9K0 ","w3V-F7iAatM ","Bh3Fw2KOA-A ","4v1fESj2oTs ","gKmqx6MXulU ","79lvSFMFWg0 ","FE80qcSfdWU ","nT2DqG7UcAg ","K0HwhC5uasI ","4opJK1CE3l8 ","ckR19VIY_Os ","Q__GLeogvao ","KL93apGPnrw ","z-x1yWODEz8 ","yyC7ghqz_pE ","vxNUUSmi88Q ","oIHTY6kx6XU ","a6WU8PFAwn0 ","bpebhYh9zes ","lmywcou0XS4 ","nTK9C6kRAUI ","Cr4_sCX8THI ","QH7pGD2sM2g ","h_axKxg2llQ ","8D-E1iRGFzo ","R59gLjcu8_Q ","6rzF3v3N9y4 ","DHpkLYYGriE ","NXbKHRU_UAU ","_g2BqoyIoJg ","Q_QoT26KGoE ","7zS5gYecCU8 ","zg544-cdY_8 ","XIuaF5x3VfE ","IqO7TtKf1h0 ","haOek69DNX0 ","ECzHU1oYLt8 ","AIsOvkkfepM ","ZY8Pq8Atp6A ","AXP15WbT2A0 ","-gOvPQLZQu4 ","HwlPgyoAn6Y ","nDfqWCQqA-E ","OgeQHZydk4E ","IvCNzxasnqw ","xFind-qzHjs ","4qtHCYEfDuE ","a2BLJF4c2Jk ","zpMgsfUGv5g ","zcpt4X4exn4 ","HKPWLVIXS4M ","5aO6J-QFL-U ","1qHia4H4Zlo ","c4eHzZDDrMk ","XrlCrb-AiRs ","-auL-_141aQ ","YE7RbUpJHjY ","a127a8g2MR0 ","p-Gvuo4cr3s ","bU2zVSRabsg ","GnbzGuUWTms ","lJhJQHKO2k4 ","uEM_MkdzEbY ","AObeTNQMBJ8 ","tGZPWo9MC9c ","mOWCBbQyRyQ ","9KP8E1Cyxkc ","hZVP7cYfH1M ","M30X_DdYos0 ","pKUhRYGvTzI ","wp3Ukt-emu0 ","2Kz5kTUxFIQ ","39moN4qjyn0 ","4lerv4G8cz4 ","TLJG1sMPiv4 ","_2-XjIreVQI ","4RIdAmGcUXQ ","JsVrfZhrJFs ","j3_RshcM0C0 ","JY8_Wz4t86I ","I5E9zVQxdv0 ","gdTWMx7fjHY ","DA9Il2rlVoQ ","v1k34e_W7wA ","nhYuYngtfYo ","vXI3A5TwCzc ","gpzHbNb-LLU ","o5fDdbBF9gc ","w5AymekJ4KM ","o-XSaDxfCxs ","_CPtXG-ZPUY ","XJurzZ3ZfQc ","MpFjGDcJ0Ec ","M6laIgkXZqQ ","Ffo1OrgcFJY ","8sUeSql--u8 ","HHJ_cGACbP8 ","_8c3Z3IL5jk ","jhwGkwNec3k ","QP2YWPbtRFE ","DpOjHy5sjg4 ","2E_SfoWNFt0 ","LBJill1wOYo ","yDAme5AjQsg ","r0L53ViQmQc ","aYpF_udKrvE ","KcJnTrQrA7s ","9y9_YbHCJFg ","gp0Zz5sd3v8 ","0q6l_xMg7fk ","KpYm1BWogDY ","wPHtAZ2CCFY ","-FqxlspUJKM ","KYc3FhTnIDE ","4z4O5JCX06Q ","g41Rojv3wTI ","T3ZbWsLtAOA ","5oOo46FF8Yw ","KEaxPbTKeoI ","IqpXa7Gv_cs ","_D50BTdXcv4 ","HgztJ88NuAc ","-_53hLaDdXw ","zG15pY8JJEI ","O8eO8nEXkm8 ","IgASHhQ1PeY ","t_SMBvWmuyg ","4WK8VzVp8JY ","cSJZWbBcQU4 ","SHPDO8qio1o ","hg_luAcEtPk ","xZCnZDvtwuE ","zCWbuxtBX7Y ","B1eEGW4kNuo ","ZAiRwEBDNfw ","3tYjnP5srag ","ongA9kbvBpc ","7zrm3MFghUo ","f3Hw66wfqwg ","YT6_6IWhFd4 ","5DUDFfYn4dU ","mXToXhQ-HvI ","5JMx2totm0U ","-dYEdvUtSFg ","cUpOQ7-1oEs ","E6VwU4kxe4g ","6_RBG5KX-Ok ","q_zXpdybQVc ","42EXAcTS7N4 ","wIYoDHA30PU ","bdUBOpyHiG4 ","QCWS3Fpg910 ","7_tj3edXEFU ","A9Nw_CHmG-Y ","Fm_d5lQSVlo ","NKtH80knbgw ","qle-Ik8Jzqc ","hlDaxqDVjZ0 ","o9eLZtKLANY ","24jriXsNBuI"]
# ["nJnZWrhQc0Y ","aH6DFIUmY_g ","LFZ2bOOhh-M ","xNj-KQkSvPY ","6i6aJ2E2H1s ","kslAcCKEuLA ","wMe9Fxpr8kw ","zGodKwJQJfA ","nfcwCL6ih8U ","Fi6iwsAgpXk ","9MIOicBGGOw ","14I2xIraVbU ","r0jA3O3i99U ","la6ob-BMuiI ","_qEr0I695sE ","feqBpHrijho ","QT-1ebN3nL8 ","-WYhK6qgWU8 ","FNlvb6l-sHs ","9pg2PbCk6Eg ","O_UY-03roZ4 ","JVFZzjoi3gY ","58OanmsYn68 ","XdFxhjHTiEc ","dmncDwKOWHM ","YLqPp9mtKIM ","eGd5_N4XMhU ","nuOP7Eta9cU ","f6ZxZMHSURE ","7LRZfM24WIk ","-81eqkOegYY ","FWQYvG-KLvQ ","rMrXSEll0WA ","wYvAi0oGArw ","9ywRRJ0QTFQ ","qP-jdMD8MuA ","_nq0bDWZIXA ","lVW0D_VCI9c ","BwPjVWX_AYA ","m0lwLWTbz0k ","OD8uHGuHrR8 ","WbQ85gXKoYM ","N3sq9gZ30kA ","NQzySRaSmXo ","k_LBcmDtWtk ","TD0sxW2Y_9s ","Xwa4k-3PNCU ","1U2Cuc_EcY4 ","9yQ_12XlKHU ","htL8mjdGERo ","VUPmV4lpr8o ","eG681R8YBqQ ","SnuaEZzJ73I ","tz_D6fY9UeE ","1Sft_Ee1YHY ","S9YFRgdZUyE ","FInr3lrkRLk ","AyytmqujX2A ","XM5scBnOnhk ","1phb3mf7AWc ","ohUNmo5ixFs ","obDslC712aE ","31_8rl1TLvM ","KOsyNlPSoKA ","jIi47ckVzuA ","3gBidS48nx4 ","MFqipJmvBqU ","en17yqTEb78 ","klMZJ1hgPGQ ","MZi2xYmZzmI ","iWvcCwkTSfs ","WvS6w-anPrg ","eBsjNQzrV9I ","fuq3REVgWMM ","7jZoN5FIMno ","OW0mLbaV3IA ","y6zwim2DiNE ","Njvd1m8fXJ4 ","tOLRQL_qU_4 ","v6mvUB1KyTU ","WctAK_a7Wb8 ","YEN8TFLxu_A ","ZsU0Up101_Q ","sjSuc-ZfOsU ","87U1g_NRg4E ","XbxTkkc6B_0 ","oTOlroZSh1g ","SXq54gvGq40 ","bgvuOstHiYM ","ppvpwhFBu7U ","dmsI9Lnv9ns ","IdH9zrg1Ty0 ","yYw4g49soAw ","o-shiBn-yt0 ","hJiBk-Z8RMs ","aUBHKKM3uNo ","K0dNQpS1n60 ","iMmmsAucMsw ","Kpa0ill3PLM ","8tlOgW2sItY ","V4NSUdP4RGU ","8bOcbTJMFbU ","ixZ7Xxv2klE ","tycNSvLLkI4 ","xj5lIi3OHeY ","Fb5zCNka_K0 ","tycNSvLLkI4 ","Fb5zCNka_K0 ","arJYjJIMY5U ","SOxVp-M5wD8 ","wtIynYJdzv4 ","iu05KZhk6IY ","Bk7Q1-IXAac ","OwjIvsxbv_s ","1WNngHHlj20 ","jD2vkj7aEmY ","lhKM78NeBoA ","0kdHbjPKfBw ","9lV2Arhfp28 ","Gh_ZX3qyw3k ","tr1VG2N0acc ","CQZWHZAOM94 ","vbyxyBZysck ","PVy6BKt7l64 ","Xxp0gRyExC0 ","FQcH08Iq8KA ","N7AMtV5Kx7o ","vwrPIf1d1AU ","5m5cqF10Z9g ","tx17P-eRsEo ","_M89onJZt1k ","JwBmpAQs1-8 ","JwBmpAQs1-8 ","lzcNu4Y0jSk ","ZFLadF8kE9M ","S8h6AYjvWtY ","bIKcvSSVZmU ","vwbwi46qS68 ","8W537DmXuXM ","15BdCfu_oVY ","ZS_RiWOvKHw ","tnOsKCENDwI ","E2GFV5_mKHQ ","9UHT16k5mjA ","rvgCOv59c60 ","8fyaNICbrq8 ","g-pBu84uy7o ","Wl0f9X_eCgY ","1Ab-kA520XA ","weWpKbs_ifU ","YQjtmzqvfmY ","jqHInicQclo ","qzkFwQfrirs ","H3kyWYUupoQ ","Gv13PwMPyyE ","fXSnGU4TpFY ","q84qlTKemcw ","Ix4vB5fubR0 ","sKM_uZ__Fsg ","L0_ZM9gUink ","Rb4fSpT2zXk ","SoDUYt0ikB4 ","T3PROkt5MDk ","VL8zFXUf2MU ","n4sSRr-vJDQ ","EOBYq4RVFgc ","e1REYV5TOuU ","SarOtNqP1os ","jgdgRakIpZg ","LhmifmNEScI ","dWkjB9JlV10 ","c4irV8QQIx0 ","g6XXz81wOmk ","_a3OdcbVYVE ","wrs0NbnQ2Xs ","BvKApPf8XBQ ","L0sNjNwIR4E ","DYYKJcYPLU8 ","1Sei1bVaP4s ","ujn2_coioWg ","VC20dsEaNmk ","AiSGWfKshHQ ","uG-oaxVTsdI ","QLMpCQH-wIo ","RumfCWkAIaI ","NN0EXOOuW3M ","P6rgy1EPxyQ ","cURO_aRx3nk ","s_hOcC5FQ9w ","k4IRVQcHOkY ","tuLpCnkkQZ4 ","Z89FT3CIFfw ","QCbW29tjPi0 ","nrVyiBdoTnU ","yRLny64xtD8 ","4Vj-eCzFqbg ","eTrb1Emf0R8 ","GFiIOEE-8lM ","81EYaDxDn54 ","2-o3tTNGeLM ","f-Bu8sMKsuQ ","hrdP4fdLlgk ","IyG9C5bK_bg ","wv9vd1FHDgM ","rKn_ehXC9Zs ","u3hHKP6fXe0 ","0JZ6Unrxpow ","fsn--iYKJAA ","Xk2z7UT1vIk ","jU3fRIq2jp4 ","nneWmdt0nt8 ","-tBkpwKfVcU ","WW1drmsd0SM ","XZPyqnPeyfA ","unqXZPwDj00 ","Ah9LtaRYIr4 ","isFlJgjyJ98 ","E-U-Kzx16MI ","5xm-IYlAWwQ ","YSazTI5blqk ","gOGfRaYLnxM ","07dPNhpbv40 ","VYl3xIAlSKk ","FmwkxO0P8lU ","q3hAMp7Cb2c ","6nfjWwhDnCs ","IaDrgrGLvUE ","wcc_8Vegqb4 ","TD36JIV_rJg ","5oyst-f3Fxs ","aP5qN-0RP-8 ","gzQKNQ8-bLI ","vPdQ_muMWdo ","EPnuvGXXSsg ","DW0X3Uxtoh0 ","VfU7GqOXooA ","Jl-j6ONkwvk ","0pz08FhJPyk ","dnFYQuVI49U ","cdPEhcMgeDU ","WINKuoQNvnU ","IZPUvAdiyck ","LCuHskOsWpg ","5MXcQjIVxBw ","a06Iz0bjU0g ","lYaQCfTuAdY ","dzz9jk3AExU ","U4iTWXQYkD0 ","Zh_pSqHxYXQ ","d94ABxH5Q2s ","AUOgkcohyyE ","C-O5XS1xkQo ","4SieBbzykHk ","zCg8J0qU6Ws ","53bQXyJ62eU ","bcWHN-hwxdQ ","R2PbTJxzGRg ","NobOHEyzYsY ","vJy9YiVjWbU ","8w6yyaQd4GU ","THiYgODMGDA ","LGEym4LuhLk ","J9Vq5JWP7Wo ","1LU71-4Hknw ","l1alFGxv-qk ","eX_MxqPKhjw ","JxDPU0Eyhgs ","pcrCrnLNi3k ","hKWBy3fIKAo ","GLU2GWKkw_U ","bSQKXGCPOP0 ","c8aTAE8EsdU ","X7wg82Qi9ZQ ","cnnCVHGzNM0 ","_qT_CYzgZ_0 ","FDhHjcoybAw ","YmoJMirU4s4 ","ErMkTTnItEA ","jxWXf62qlBg ","x-3TzQszLUM ","Yqy1xWM2Vpk ","mDms5YAqMEQ ","TU2XOmeExU4 ","9eY9iDWzOeM ","hH4NCOQluLo ","DfVqEsDT6y8 ","9c1GX35O-kw ","sswTAvhnCCM ","8zgVDqwk1rY ","hV1MUYNn3eA ","fPNWJPNPplU ","smkIZWWL-qM ","jGIW3I6YKYI ","pzd1CFHqymM ","X1QtDMM3PxE ","uDvZzVLwP68 ","bE29hzO2uQk ","vsIh7r62TVk ","cLnfvW-P5fw ","Wq-UQbJLIS8 ","hdSNXXlJH7w ","_iX8rIvykwg ","s5ZKCO4vdT8 ","hrbTf2Qpd1A ","IYALJnNvSvA ","dcGDtkkrolo ","lRPX12cVDKA ","8kbQ-mF4M-g ","_z8ZiDezbL8 ","OOkCp6bHmJQ ","M7sgy5aJ87I ","xghTCsjG0W0 ","iEXXa2qsV9E ","IV1jFMWT_Yw ","oduRCjRYsh4 ","zwIHjAwm2GM ","6ZynfSGdoVg ","Mu27y5-_4WI ","-Atecifkw28 ","a0jNA4lE5Zo ","dIFgMycmFhk ","lgjh2wQ5vBc ","Xp9MZDzSLh0 ","oH97rXUMkgk ","rd_ajJ1m-pQ ","-PGVU3jDFmI ","ucoh1T_WY-c ","CnPpTRSC3rA ","e0c-ftwgSWA ","XI1eT9XhPpM ","n2PacZL8RNc ","zCW1cTpyIeg ","qEUewspoLGE ","hUihFuM_Dlw ","JtzxkyIKoks ","1p19YqlRovM ","PbCxXqlp1ek ","mc1yl7AQnAI ","zOe9i7xYxrQ ","l8aBAU7CGcc ","J8rt5djpeLU ","3mxxgQTUsiU ","Aw6F5cNrnJU ","0OVlmhIcLo0 ","gUt0a7EHZ7E ","P8iabaUsVIY ","TF_UiYnNgeA ","J24ALQ4c-_A ","8JjXjekqgXA ","0_kYt0wGg1I ","pFEI0u9ctJw ","gsNGsn8hLA0 ","rVOUgZY0MhY ","fxlU0wRZr5I ","TcLx3fmnGA8 ","FGyT5NhD1TM ","0gTzpNVspts ","Bbsr0S0rA1Y ","xXP1Pa0H6fI ","Y8XktCi_-Hw ","ZN1ysdBlR3c ","QoFDZy7U91M ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g ","HbQ6zZOehSU ","XflIDniiJ_g ","VT5GDTlvVks ","fHbCYHZIyvQ ","SrPuDXDkA5M ","HumBTko05mk ","e44V8Z8DYRI ","2wkoSCOmll4 ","SzXOsq6f-2g"]


video_id_list=["GQ3kDpQLJEk ","XSouBnZS7rM ","rPB6bm_6obQ ","KVWMbxJGkpk ","xy2IIEO6T3E ","kqTRDPeUxZ0 ","R4O2GH1EmjA ","eknvy7bFXZs ","g_dzzXzYDvY ","fz_SnOtNSsI ","ysCw9gRsF6c ","AeFiuT3WdQg ","RbyvklCUn3w ","Cx2YW4DgGKE ","ove0WNIYJ_w ","lSwKKuCZTSA ","oBEaiTDb5RQ ","psP84DkP1Pk ","I62E_X4aq0w ","S0lOoJs-QSg ","nTDZywQ7W6k ","LyQcTBomv5Y ","ZtPpDYaBAR8 ","XqYg4ZgI2Oo ","ZL4SC_sk9aM ","BnHjNlyXorQ ","upCZ9RiOkOk ","6jPVNDxJ3PQ ","t13jxn5XGo0 ","azcopDKvmBg ","lkvNGu4bD3w ","QSzbTehBl1Y ","_P8IrbjSLlo ","T1YUDw5GG0c ","_n10MpYzEZI ","Esmf7a7309U ","tX1op3pExf4 ","2IC5onszdEQ ","Iy5ryDM4nKI ","p3dA38T5WV8 ","xx2VbvKj5NA ","nHvjSivJoJo ","BE3pFaY6oHU ","zzRAY6RDx9s ","jhX-RJq8zCs ","N3nMH2Io1FQ ","I253t4KW1NI ","1d-2p2I7_Kc ","PCRMAgbUkN8 ","FOI70ZcfEjI ","ZR8Rp5d2WMQ ","95vbrTdaDEM ","ODSkxlwprz0 ","M2ZzniVS2rk ","aXWA1BR1Klg ","1jOaRS2shyY ","FlsTRqaJaOo ","dDFmgYHcDVI ","63imUuEHUKA ","Kkju7XQvFMg ","wIrKq3aKNnQ ","L_TAM8hzLPs ","yprSX1aIL2g ","SH_50Gfpmrk ","LrHtKEVLG-E ","ckFKEI6fWdM ","_Vw6YuUheG0 ","7_Mu4qIXFss ","q_gjJhxB9lw ","hArhTKEl0Uo ","FVjyc5ykqRY ","DGBPOyngF7k ","ZXZmM9GQf78 ","_dQryJPNSzU ","wA9uWei8gX4 ","Xjob6AJWWiI ","5MTauI86Jrg ","b48XIKcPzhU ","BAGcpo0xfZU ","AQ77M0Re7cI ","riPKeBgADLw ","qYdU7CCafeY ","MPCB9k2dO6Y ","ggXhceK8pLw ","cjokxHPwmmY ","svi9Qv7YDb4 ","fDcGZnevd_A ","JqohAO0IWx8 ","QOAAFCPiNRw ","knTBNH5RY7U ","He--pu9K93w ","ggFIT4NfK6k ","C1A3HhfusFc ","lWDRfBlza_0 ","r81Wd4BsiPA ","vQS3M5Xu8HA ","6ctzUqTrEhY ","ht4DHMCuGzI ","blCA7dSHHok ","Vy9Qz3PT4b0 ","1HqkPmtNUcU ","fdGK-fufvWI ","pY5LaV2DsHo ","H2WQipl5EP8 ","JKndZYn2rH4 ","Bzfd__Hq0Tc ","jduixCXEFHk ","UJ0zJHHsOIU ","2G2SA1taeYA ","6xIr6WnmMiE ","Q4tQ3eN5QEI ","ExRfW9oZdls ","MweSzQtV3uM ","FSYcZq7cVDY ","NAGYPaE_lqs ","oKfVbXIc_Ko ","zGzXRBNMdYg ","UsX4X0Q3zPE ","QYu5-gmG9j8 ","7YtaN0vEyRk ","5PBHOYo6P4U ","w6o9bbYfjD0 ","j-vv2trH5yc ","jLFG9B10DxM ","A7y0VwzLW9g ","N1YhPABDytc ","0VSG9HEtJVw ","9-cne-0QKwo ","7bHS_Bw9X74 ","sSZjg8UsM6M ","5nY6Kdwr9Mo ","dV0F7rfDtDk ","Ddvz7DHfzxA ","leyb4vrLCHk ","VSfKATpgbKk ","4io-Z2F5bxY ","RJhm6iMe5iI ","eULXDmJ6aGg ","103ajYWWWE8 ","Ke8b3eza0Js ","qhSjDvWwVok ","raQ7jAVrX9Y ","BkVNiFoWxrw ","aa5LYa89xd8 ","h54wetfwqQg ","7oQGrGocUBg ","5CEm1S8teNE ","2JJSHZFn_Ok ","S86YT9e-lNA ","FNbUdSkWSBw ","AZVs2L3lDOI ","DC6VHihmPLQ ","IFTJFlgJXio ","ivli9Ic8gXk ","Q_X_rYeOMUs ","NwToSXbnWKo ","fHRXcSjM1QY ","tcj9TMUM5QM ","trXbDTFnDy4 ","Paa6YeM-L2U ","MsF0K_G1WUg ","n4KB9GHdu-s ","73KTW1TCqqk ","LGJomOUunDA ","AN18wT9lMzM ","7JVlMhTlwT4 ","uaCbp3G7vHs ","kJ4s3G7hgR4 ","75kQrsEA1qk ","HHMToqWZxg0 ","lB6laDgEzbQ ","ksKOWhDe48c ","NUPISuGlcP8 ","dLmeGbYNW9k ","OoTSoEQ8TF4 ","oDedQqATUP4 ","rH7SpPTUARc ","aly6i_J-MhU ","VfXlnstcMXQ ","V7jCLEPUglo ","ZjNXlY-p8qc ","UeZAMBolhm0 ","br40gTEYNGs ","Q__GLeogvao ","oHylZDdL1cw ","qbl1mJpqbhQ ","Yx785mVTYrQ ","5bpPfCPE9oc ","Kf5kIiWKDmw ","YtmZb5SxSZA ","SCWQTbuHRtI ","w_1kaMt_Ako ","jSgZteOobvI ","-JFiFnTXeVU ","NupKqka1SF4 ","K38tMOFP9pc ","VrUCFtwooTs ","cR8icB7Vem8 ","t6kfKQLCmm8 ","19qrJfum5wo ","H4-2CB2qqrs ","xgWAem967Lw ","3RijnSj0vN4 ","xiqsn6pjZeY ","wSsdwVhlZq4 ","QKZ9zX9vons ","WIotm9ZlGjU ","5KYinte7Ykc ","fyTe5kYl9TE ","Cf6nwwBoh3g ","zWYwf_a7nQg ","ZtHqTDyLQr0 ","gyuHIBK25cw ","pX0fN_pHJ6A ","jeeTrbmqW78 ","Rf983q93jRw ","EAOfJlWuvd8 ","mmZqx6WAQZU ","FQw9-0Ygrpg ","9r3jvvc7AMU ","za_GRedXhhQ ","5hidTa_lezs ","C7m02AuDjN8 ","_Ehuugy1dZs ","tTVNOqi4uOg ","HRMC9HTcoKU ","OwcYDVL6NV4 ","aH9Uraf4iTk ","CXa8wKJG6X4 ","CVNWVwxx1fk ","GDCu3ms9zsQ ","u-1NF_pHm7U ","RTlqrbyNaZ4 ","K5HFewun2YY ","Eec5x1pI1mU ","qryJ166ApOg ","bQFe6PfGG-I ","XHQcqUWuGME ","gyWH4umVvx8 ","r1pGe2pAXpU ","O-0nx4n7Bu0 ","S9qnMDNfLlY ","elcxHZv2M0o ","0wt9CXPGLwo ","xywrg-mUsxI ","UwNPKpaBYJ4 ","nAXyvn07FYE ","A8xhTMC4KO0 ","OXCt_-ChwP0 ","1BVHjyTr0-Q ","rD0SiiZTkkg ","n9tMTdJsOJk ","RtNnfbEPUbQ ","gOo4pidzAZM ","htIJjxXFLbg ","xnbmhaSTVBQ ","xgd4_lCLj8E ","I3nQK0J5Olo ","scdvW83kzPs ","4KNhkDTksGk ","hE5Lw3zg8Ik ","u9JSp6I76eg ","O3V0bNI3uF4 ","GWCTFrQ753s ","4DLbTsG6EaQ ","NuIV7pd7oVQ ","pW9bb6FzQ4I ","H_qXxvNr-zM ","qabM0G8L2tY ","FTruJTRu-VQ ","zOoLLkNqe9g ","ZC5jlrso9nA ","hwNH4VAYSS4 ","uZKfXR44P8s ","qb5gt-nQ6RE ","9SzK59wnEtE ","OlYMS9tXUVM ","u_tALjufHes ","sTIUwnGG--8 ","HSnXnCqReBw ","8hIj3PVGnI0 ","rteB4bQm5QQ ","cGiB3QiK_MQ ","_Xy_2V-9oms ","d7_r4eICauE ","spV34dlKfyw ","Qvyug26LtgI ","i-HlabhrcIQ ","8W9Xy00NGNA ","oEeJVSgJdZg ","soDRYei03hM ","zYwCgZ4m4A0 ","_-iM1xxD6YM ","kzTRKx5l48A ","l2_GDUQQj2I ","5qmOI01cDXI ","5hjlBq3FuaU ","JeZQgtfufwA ","nJOOYjrKyI4 ","7NeUB_oEhSg ","MoND9QE9uDA ","a3pci7i_YOk ","WGEj8774JNY ","Y31_1hZpl9s ","_uq3SXhnNio ","kX28JSBlRDk ","Tjd8IarH4S4 ","-Xdp7jD4N9k ","2IgfRHhhv8A ","7lNDXsnsZ_I ","NaCKuT_DEMY ","dMtaF8vWUyU ","gC6xkeeKJYE ","JBNwZ_FmKWs ","_M8WjMe64-g ","8aKTKgF9c94 ","rI8ovMlbxc4 ","SUBUj5mQBvA ","BmzZOtHj9Rc ","22dgj47LU3o ","59pmoLiQMg8 ","I3LEylQX57k ","IVbI6g-Uh6E ","IERQ01n6FUY ","bwmCxMqkvl0 ","9XEbKNg9XcI ","Zpbyw-MxY_4 ","PeY6q_k_n6I ","6OTdM8HDIr0 ","PYW4aMSdvek ","KuD7kjFageQ ","eKm8WtWJNNw ","vqDAigwGrgY ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk ","qNSy0Ko9-9c ","ddAXlN-8gIc ","SJdZ4jF9MnU ","P467LJKioRE ","txtSfqFuBVA ","4ae12ivt6zk"]



'''
	Helper to transform GET parameters into dict objects
'''
def get_inline_params(request,key='params'):
	if key in request.GET:
		params = json.loads(request.GET.get(key))
	else:
		params = request.GET.dict()
	return params


# Create your views here.

def index(request):
	if request.POST:
		#screenshot()
		query= request.POST['query']

		# Metodo per interfacciarsi con youtube
		# Idealmente il sistema dovrebbe lanciare la funzione di screenshot per ogni video sospetto 
		# una volta scaricato lo screenshot (o elaborato in memoria)
		# il sistema deve aggiungere il codice del video alla lista dei video sospetti
		#results= blockspring.runParsed("youtube-video-search", { "query": query }, {"api_key":"br_24571_0ec006b950d2de2d74f7bb53a97f71404fb34595"}).params

		#for i in results:
		#	print(i)

	else:
		query=""
	

	context = {
		'query_value' : query,
	}

	
	return render_to_response('paladin/search.html',context,context_instance=RequestContext(request))


def multiQuery(request):
	results= blockspring.runParsed("youtube-video-search", { "query": query }, {"api_key":"br_24571_0ec006b950d2de2d74f7bb53a97f71404fb34595"}).params
	for i in results:
		print(i)

	
	context = {
		'query_value' : query,
	}

	
	return render_to_response('paladin/search.html',context,context_instance=RequestContext(request))




def monitoraggio(request):
	print("Monitoraggio")
	query_list=Query.objects.all()

	context = {
		'query_list' : query_list,
	}
	return render_to_response('paladin/monitoraggio.html',context,context_instance=RequestContext(request))


def statistiche(request):
	print("Statistiche")
	return render_to_response('paladin/statistiche.html')


def getScreenshot(fox,video):

	print(video)
	#fox.get('http://stackoverflow.com/')
	sleep(25)
	try:
		fox.find_element_by_css_selector("button.videoAdUiSkipButton.videoAdUiAction").click()
	except:
		print("Skip not present")

	# now that we have the preliminary stuff out of the way time to get that image :D
	#element = fox.find_element_by_id('placeholder-player') # find part of the page you want image of
	#fox.save_screenshot("pagina_completa"+video+'.png')
	
	element = fox.find_element_by_css_selector('div.player-api.player-width.player-height') # find part of the page you want image of
	
	location = element.location
	size = element.size
	fox.get_screenshot_as_file(video+'.png') # saves screenshot of entire page
	
	im = Image.open(video+'.png') # uses PIL library to open image in memory




	left = location['x']
	top = location['y']
	right = location['x'] + size['width']
	bottom = location['y'] + size['height']

	im = im.crop((left, top, right, bottom)) # defines crop points
	im.save(video+'.png') # saves new cropped image

	


def screenshot(request,video_id="1"):
			
	# esempio yfdKc4JM0BY
	site = "https://www.youtube.com/watch?v="
	
	#timing="?t=15s"
	delay = 15
	fox = webdriver.Firefox()
	fox.implicitly_wait(3)

	fox.get(site+video_id+"&feature=youtu.be&t="+str(delay)+"s")

	getScreenshot(fox,video_id)
	fox.quit()
	
	image_data = open(video_id+".png", "rb").read()
	
	context = {
		'frame' : video_id+".png"
	}

	
	return HttpResponse(image_data, content_type="image/png")


''' da una lista di link di video estrae gli screenshots'''
def multipleScreenshots(request):
			
	# esempio yfdKc4JM0BY
	site = "https://www.youtube.com/watch?v="
	
	#timing="?t=15s"
	delay = 15
	fox = webdriver.Firefox()
	for video_id in video_id_list:
		fox.implicitly_wait(3)

		fox.get(site+video_id+"&feature=youtu.be&t="+str(delay)+"s")

		getScreenshot(fox,video_id)
	fox.quit()
	

	
	return HttpResponse("done")





