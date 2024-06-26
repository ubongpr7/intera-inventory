# Generated by Django 4.2.13 on 2024-06-08 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainapps.common.settings
import mainapps.inventory.helpers.field_validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(default='333898107722661', editable=False, max_length=15, unique=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Company name')),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('description', models.CharField(blank=True, help_text='Briefly describe the company', max_length=1000, null=True, verbose_name='Company description')),
                ('website', models.URLField(blank=True, help_text='Company website URL (optional)', verbose_name='Website')),
                ('phone', models.CharField(blank=True, help_text='Contact phone number (optional)', max_length=15, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, help_text='Contact email address (optional)', max_length=254, null=True, verbose_name='Email')),
                ('link', models.URLField(blank=True, help_text='Link to external company information or profile', verbose_name='Link/Website')),
                ('currency', models.CharField(blank=True, choices=[('AFN', 'AFGHANI'), ('EUR', 'EURO'), ('ALL', 'LEK'), ('DZD', 'ALGERIAN DINAR'), ('USD', 'US DOLLAR'), ('AOA', 'KWANZA'), ('XCD', 'EAST CARIBBEAN DOLLAR'), ('ARS', 'ARGENTINE PESO'), ('AMD', 'ARMENIAN DRAM'), ('AWG', 'ARUBAN FLORIN'), ('AUD', 'AUSTRALIAN DOLLAR'), ('AZN', 'AZERBAIJAN MANAT'), ('BSD', 'BAHAMIAN DOLLAR'), ('BHD', 'BAHRAINI DINAR'), ('BDT', 'TAKA'), ('BBD', 'BARBADOS DOLLAR'), ('BYN', 'BELARUSIAN RUBLE'), ('BZD', 'BELIZE DOLLAR'), ('BMD', 'BERMUDIAN DOLLAR'), ('INR', 'INDIAN RUPEE'), ('BTN', 'NGULTRUM'), ('BOP', 'BOLIVIAN PESO'), ('BOB', 'BOLIVIANO'), ('BWP', 'PULA'), ('NOK', 'NORWEGIAN KRONE'), ('BRL', 'BRAZILIAN REAL'), ('BND', 'BRUNEI DOLLAR'), ('BGN', 'BULGARIAN LEV'), ('BIF', 'BURUNDI FRANC'), ('CVE', 'CABO VERDE ESCUDO'), ('KHR', 'RIEL'), ('CAD', 'CANADIAN DOLLAR'), ('KYD', 'CAYMAN ISLANDS DOLLAR'), ('CLP', 'CHILEAN PESO'), ('CNY', 'YUAN RENMINBI'), ('COP', 'COLOMBIAN PESO'), ('KMF', 'COMORIAN FRANC '), ('CDF', 'CONGOLESE FRANC'), ('NZD', 'NEW ZEALAND DOLLAR'), ('CRC', 'COSTA RICAN COLON'), ('XOF', 'CFA FRANC BCEAO'), ('CUP', 'CUBAN PESO'), ('ANG', 'NETHERLANDS ANTILLEAN GUILDER'), ('CZK', 'CZECH KORUNA'), ('DKK', 'DANISH KRONE'), ('DJF', 'DJIBOUTI FRANC'), ('DOP', 'DOMINICAN PESO'), ('EGP', 'EGYPTIAN POUND'), ('SVC', 'EL SALVADOR COLON'), ('ERN', 'NAKFA'), ('SZL', 'LILANGENI'), ('ETB', 'ETHIOPIAN BIRR'), ('FKP', 'FALKLAND ISLANDS POUND'), ('FJD', 'FIJI DOLLAR'), ('GMD', 'DALASI'), ('GEL', 'LARI'), ('GHS', 'GHANA CEDI'), ('GIP', 'GIBRALTAR POUND'), ('GTQ', 'QUETZAL'), ('GBP', 'POUND STERLING'), ('GNF', 'GUINEAN FRANC'), ('GYD', 'GUYANA DOLLAR'), ('HTG', 'GOURDE'), ('HNL', 'LEMPIRA'), ('HKD', 'HONG KONG DOLLAR'), ('HUF', 'FORINT'), ('ISK', 'ICELAND KRONA'), ('IDR', 'RUPIAH'), ('IRR', 'IRANIAN RIAL'), ('IQD', 'IRAQI DINAR'), ('ILS', 'NEW ISRAELI SHEQEL'), ('JMD', 'JAMAICAN DOLLAR'), ('JPY', 'YEN'), ('JOD', 'JORDANIAN DINAR'), ('KZT', 'TENGE'), ('KES', 'KENYAN SHILLING'), ('KPW', 'NORTH KOREAN WON'), ('KRW', 'WON'), ('KWD', 'KUWAITI DINAR'), ('KGS', 'SOM'), ('LAK', 'LAO KIP'), ('LBP', 'LEBANESE POUND'), ('LSL', 'LOTI'), ('ZAR', 'RAND'), ('LRD', 'LIBERIAN DOLLAR'), ('LYD', 'LIBYAN DINAR'), ('CHF', 'SWISS FRANC'), ('MOP', 'PATACA'), ('MKD', 'DENAR'), ('MYR', 'MALAYSIAN RINGGIT'), ('MVR', 'RUFIYAA'), ('MUR', 'MAURITIUS RUPEE'), ('MXN', 'MEXICAN PESO'), ('MDL', 'MOLDOVAN LEU'), ('MNT', 'TUGRIK'), ('MAD', 'MOROCCAN DIRHAM'), ('MZN', 'MOZAMBIQUE METICAL'), ('MMK', 'KYAT'), ('NAD', 'NAMIBIA DOLLAR'), ('NPR', 'NEPALESE RUPEE'), ('OMR', 'RIAL OMANI'), ('PKR', 'PAKISTAN RUPEE'), ('PHP', 'PHILIPPINE PESO'), ('PLN', 'ZLOTY'), ('QAR', 'QATARI RIAL'), ('RON', 'ROMANIAN LEU'), ('RUB', 'RUSSIAN RUBLE'), ('RWF', 'RWANDA FRANC'), ('SHP', 'SAINT HELENA POUND'), ('SAR', 'SAUDI RIYAL'), ('RSD', 'SERBIAN DINAR'), ('SCR', 'SEYCHELLES RUPEE'), ('SLL', 'LEONE'), ('SLE', 'LEONE'), ('SGD', 'SINGAPORE DOLLAR'), ('SBD', 'SOLOMON ISLANDS DOLLAR'), ('SOS', 'SOMALI SHILLING'), ('SSP', 'SOUTH SUDANESE POUND'), ('LKR', 'SRI LANKA RUPEE'), ('SDG', 'SUDANESE POUND'), ('SRD', 'SURINAM DOLLAR'), ('SEK', 'SWEDISH KRONA'), ('SYP', 'SYRIAN POUND'), ('TWD', 'NEW TAIWAN DOLLAR'), ('TJS', 'SOMONI'), ('TZS', 'TANZANIAN SHILLING'), ('THB', 'BAHT'), ('TTD', 'TRINIDAD AND TOBAGO DOLLAR'), ('TND', 'TUNISIAN DINAR'), ('TRY', 'TURKISH LIRA'), ('TMT', 'TURKMENISTAN NEW MANAT'), ('UGX', 'UGANDA SHILLING'), ('UAH', 'HRYVNIA'), ('AED', 'UAE DIRHAM'), ('UZS', 'UZBEKISTAN SUM'), ('VES', 'BOLÍVAR SOBERANO'), ('VED', 'BOLÍVAR SOBERANO'), ('YER', 'YEMENI RIAL'), ('ZMW', 'ZAMBIAN KWACHA'), ('ZWL', 'ZIMBABWE DOLLAR'), ('VND', 'DONG'), ('NGN', 'NAIRA'), ('VUV', 'VATU'), ('PAB', 'BALBOA'), ('PGK', 'KINA'), ('PYG', 'GUARANI'), ('PEN', 'SOL'), ('WST', 'TALA'), ('STN', 'DOBRA'), ('MGA', 'MALAGASY ARIARY'), ('MWK', 'MALAWI KWACHA'), ('MRU', 'OUGUIYA'), ('UYU', 'PESO URUGUAYO'), ('TOP', "PA'ANGA"), ('NIO', 'NICARAGUAN CÓRDOBA'), ('CUC', 'PESO CONVERTIBLE'), ('BAM', 'CONVERTIBLE MARK'), ('XPF', 'CFP FRANC'), ('XAF', 'CFA FRANC BEAC'), ('BTC', 'BITCOIN'), ('XBT', 'BITCOIN'), ('LTC', 'LITECOIN'), ('NMC', 'NAMECOIN'), ('PPC', 'PEERCOIN'), ('XRP', 'RIPPLE'), ('DOGE', 'DOGECOIN'), ('GRC', 'GRIDCOIN'), ('XPM', 'PRIMECOIN'), ('OMG', 'OMG NETWORK'), ('NXT', 'NXT'), ('AUR', 'AURORACOIN'), ('BLZ', 'BLUZELLE'), ('DASH', 'DASH'), ('NEO', 'NEO'), ('MZC', 'MAZACOIN'), ('XMR', 'MONERO'), ('TIT', 'TITCOIN'), ('XVG', 'VERGE'), ('VTC', 'VERTCOIN'), ('XLM', 'STELLAR'), (None, 'COINYE'), ('ETH', 'ETHEREUM'), ('ETC', 'ETHEREUM CLASSIC'), ('XNO', 'NANO'), ('USDT', 'TETHER'), (None, 'ONECOIN'), ('FIRO', 'FIRO'), ('ZEC', 'ZCASH'), ('ZRX', '0X'), ('AAVE', 'AAVE'), ('BNT', 'BANCOR'), ('BAT', 'BASIC ATTENTION TOKEN'), ('BCH', 'BITCOIN CASH'), ('BTG', 'BITCOIN GOLD'), ('BNB', 'BINANCE COIN'), ('ADA', 'CARDANO'), ('COTI', 'COTI'), ('LINK', 'CHAINLINK'), ('MANA', 'DECENTRALAND'), ('ENS', 'ETHEREUM NAME SERVICE'), ('EOS', 'EOS.IO'), ('ENJ', 'ENJIN'), ('FET', 'FETCH.AI'), ('NMR', 'NUMERAIRE'), ('MLN', 'MELON'), ('MATIC', 'POLYGON'), ('STORJ', 'STORJ'), ('LRC', 'LOOPRING'), ('BCC', 'BITCONNECT'), (None, 'AMBACOIN'), ('ACH', 'ALCHEMY PAY'), ('BSV', 'BITCOIN SV'), ('CRO', 'CRONOS'), ('FTM', 'FANTOM'), ('CKB', 'NERVOS NETWORK'), ('USTC', 'TERRACLASSICUSD'), ('LUNA', 'TERRA'), ('USDC', 'USD COIN'), ('UNI', 'UNISWAP'), ('MDT', 'MEASURABLE DATA TOKEN'), ('SNX', 'SYNTHETIX'), ('QNT', 'QUANT'), (None, 'KODAKCOIN'), ('PTR', 'PETRO'), ('ALGO', 'ALGORAND'), ('ANKR', 'ANKR'), ('AXS', 'AXIE INFINITY'), ('BAND', 'BAND PROTOCOL'), ('BICO', 'BICONOMY'), ('BUSD', 'BINANCE USD'), ('ATOM', 'COSMOS'), ('CHZ', 'CHILIZ'), ('OXT', 'ORCHID'), ('TRB', 'TELLOR'), ('WBTC', 'WRAPPED BITCOIN'), ('1INCH', '1INCH NETWORK'), ('AVAX', 'AVALANCHE'), ('API3', 'API3'), ('AMP', 'AMP'), ('BAL', 'BALANCER'), ('BOND', 'BARNBRIDGE'), ('FIDA', 'BONFIDA'), ('BCHA', 'BITCOIN CASH ABC'), ('CELO', 'CELO'), ('COMP', 'COMPOUND'), ('CRV', 'CURVE'), ('FIL', 'FILECOIN'), ('CAKE', 'PANCAKESWAP'), ('DOT', 'POLKADOT'), ('MIR', 'MIRROR PROTOCOL'), ('GRT', 'THE GRAPH'), ('SHIB', 'SHIBA INU'), ('SOL', 'SOLANA'), ('SUSHI', 'SUSHISWAP'), ('YFI', 'YEARN.FINANCE'), ('FORTH', 'AMPLEFORTH GOVERNANCE TOKEN'), ('BIT', 'BITDAO'), ('CTSI', 'CARTESI'), ('DESO', 'DECENTRALIZED SOCIAL'), ('SFM', 'SAFEMOON'), ('APE', 'APECOIN'), ('APT', 'APTOS'), ('XPD', 'PALLADIUM'), ('XPT', 'PLATINUM'), ('XAU', 'GOLD'), ('XAG', 'SILVER'), ('XSU', 'SUCRE'), ('XDR', 'SDR (SPECIAL DRAWING RIGHT)'), ('XUA', 'ADB UNIT OF ACCOUNT'), ('XBA', 'BOND MARKETS UNIT EUROPEAN COMPOSITE UNIT (EURCO)'), ('XBB', 'BOND MARKETS UNIT EUROPEAN MONETARY UNIT (E.M.U.-6)'), ('XBC', 'BOND MARKETS UNIT EUROPEAN UNIT OF ACCOUNT 9 (E.U.A.-9)'), ('XBD', 'BOND MARKETS UNIT EUROPEAN UNIT OF ACCOUNT 17 (E.U.A.-17)'), ('XXX', 'THE CODES ASSIGNED FOR TRANSACTIONS WHERE NO CURRENCY IS INVOLVED'), ('MXV', 'MEXICAN UNIDAD DE INVERSION (UDI)'), ('USN', 'US DOLLAR (NEXT DAY)'), ('UYW', 'UNIDAD PREVISIONAL'), ('CHE', 'WIR EURO'), ('CHW', 'WIR FRANC'), ('UYI', 'URUGUAY PESO EN UNIDADES INDEXADAS (UI)'), ('BOV', 'MVDOL'), ('CLF', 'UNIDAD DE FOMENTO'), ('COU', 'UNIDAD DE VALOR REAL')], default=mainapps.common.settings.DEFAULT_CURRENCY_CODE, help_text='Set company default currency', max_length=12, validators=[mainapps.inventory.helpers.field_validators.validate_currency_code], verbose_name='Base Currency')),
                ('industry', models.ForeignKey(limit_choices_to={'which_model': 'industry'}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.typeof')),
                ('owner', models.OneToOneField(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Company Profile',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PrescriptionFillingPolicies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Policy name')),
                ('details', models.TextField(unique=True, verbose_name='Details of the policy')),
                ('effective_date', models.DateField(null=True)),
                ('expiration_date', models.DateField(null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('validity_period', models.IntegerField(default=5, help_text='Prescription is valid before how many days')),
                ('quantitity_limit', models.IntegerField()),
                ('refills_allowed', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.companyprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddConstraint(
            model_name='companyprofile',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_name'),
        ),
    ]
