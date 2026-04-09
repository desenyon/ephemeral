"""Round-trip tests for generated Pydantic payloads."""
from ephemeral.validation.generated import payloads as gp


def test_gen_payload_0000_roundtrip():
    m = gp.GenPayload0000(tag='t', score=0)
    d = m.model_dump()
    m2 = gp.GenPayload0000.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 0

def test_gen_payload_0003_roundtrip():
    m = gp.GenPayload0003(tag='t', score=3)
    d = m.model_dump()
    m2 = gp.GenPayload0003.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 3

def test_gen_payload_0006_roundtrip():
    m = gp.GenPayload0006(tag='t', score=6)
    d = m.model_dump()
    m2 = gp.GenPayload0006.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 6

def test_gen_payload_0009_roundtrip():
    m = gp.GenPayload0009(tag='t', score=9)
    d = m.model_dump()
    m2 = gp.GenPayload0009.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 9

def test_gen_payload_0012_roundtrip():
    m = gp.GenPayload0012(tag='t', score=12)
    d = m.model_dump()
    m2 = gp.GenPayload0012.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 12

def test_gen_payload_0015_roundtrip():
    m = gp.GenPayload0015(tag='t', score=15)
    d = m.model_dump()
    m2 = gp.GenPayload0015.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 15

def test_gen_payload_0018_roundtrip():
    m = gp.GenPayload0018(tag='t', score=1)
    d = m.model_dump()
    m2 = gp.GenPayload0018.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 1

def test_gen_payload_0021_roundtrip():
    m = gp.GenPayload0021(tag='t', score=4)
    d = m.model_dump()
    m2 = gp.GenPayload0021.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 4

def test_gen_payload_0024_roundtrip():
    m = gp.GenPayload0024(tag='t', score=7)
    d = m.model_dump()
    m2 = gp.GenPayload0024.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 7

def test_gen_payload_0027_roundtrip():
    m = gp.GenPayload0027(tag='t', score=10)
    d = m.model_dump()
    m2 = gp.GenPayload0027.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 10

def test_gen_payload_0030_roundtrip():
    m = gp.GenPayload0030(tag='t', score=13)
    d = m.model_dump()
    m2 = gp.GenPayload0030.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 13

def test_gen_payload_0033_roundtrip():
    m = gp.GenPayload0033(tag='t', score=16)
    d = m.model_dump()
    m2 = gp.GenPayload0033.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 16

def test_gen_payload_0036_roundtrip():
    m = gp.GenPayload0036(tag='t', score=2)
    d = m.model_dump()
    m2 = gp.GenPayload0036.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 2

def test_gen_payload_0039_roundtrip():
    m = gp.GenPayload0039(tag='t', score=5)
    d = m.model_dump()
    m2 = gp.GenPayload0039.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 5

def test_gen_payload_0042_roundtrip():
    m = gp.GenPayload0042(tag='t', score=8)
    d = m.model_dump()
    m2 = gp.GenPayload0042.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 8

def test_gen_payload_0045_roundtrip():
    m = gp.GenPayload0045(tag='t', score=11)
    d = m.model_dump()
    m2 = gp.GenPayload0045.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 11

def test_gen_payload_0048_roundtrip():
    m = gp.GenPayload0048(tag='t', score=14)
    d = m.model_dump()
    m2 = gp.GenPayload0048.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 14

def test_gen_payload_0051_roundtrip():
    m = gp.GenPayload0051(tag='t', score=0)
    d = m.model_dump()
    m2 = gp.GenPayload0051.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 0

def test_gen_payload_0054_roundtrip():
    m = gp.GenPayload0054(tag='t', score=3)
    d = m.model_dump()
    m2 = gp.GenPayload0054.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 3

def test_gen_payload_0057_roundtrip():
    m = gp.GenPayload0057(tag='t', score=6)
    d = m.model_dump()
    m2 = gp.GenPayload0057.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 6

def test_gen_payload_0060_roundtrip():
    m = gp.GenPayload0060(tag='t', score=9)
    d = m.model_dump()
    m2 = gp.GenPayload0060.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 9

def test_gen_payload_0063_roundtrip():
    m = gp.GenPayload0063(tag='t', score=12)
    d = m.model_dump()
    m2 = gp.GenPayload0063.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 12

def test_gen_payload_0066_roundtrip():
    m = gp.GenPayload0066(tag='t', score=15)
    d = m.model_dump()
    m2 = gp.GenPayload0066.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 15

def test_gen_payload_0069_roundtrip():
    m = gp.GenPayload0069(tag='t', score=1)
    d = m.model_dump()
    m2 = gp.GenPayload0069.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 1

def test_gen_payload_0072_roundtrip():
    m = gp.GenPayload0072(tag='t', score=4)
    d = m.model_dump()
    m2 = gp.GenPayload0072.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 4

def test_gen_payload_0075_roundtrip():
    m = gp.GenPayload0075(tag='t', score=7)
    d = m.model_dump()
    m2 = gp.GenPayload0075.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 7

def test_gen_payload_0078_roundtrip():
    m = gp.GenPayload0078(tag='t', score=10)
    d = m.model_dump()
    m2 = gp.GenPayload0078.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 10

def test_gen_payload_0081_roundtrip():
    m = gp.GenPayload0081(tag='t', score=13)
    d = m.model_dump()
    m2 = gp.GenPayload0081.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 13

def test_gen_payload_0084_roundtrip():
    m = gp.GenPayload0084(tag='t', score=16)
    d = m.model_dump()
    m2 = gp.GenPayload0084.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 16

def test_gen_payload_0087_roundtrip():
    m = gp.GenPayload0087(tag='t', score=2)
    d = m.model_dump()
    m2 = gp.GenPayload0087.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 2

def test_gen_payload_0090_roundtrip():
    m = gp.GenPayload0090(tag='t', score=5)
    d = m.model_dump()
    m2 = gp.GenPayload0090.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 5

def test_gen_payload_0093_roundtrip():
    m = gp.GenPayload0093(tag='t', score=8)
    d = m.model_dump()
    m2 = gp.GenPayload0093.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 8

def test_gen_payload_0096_roundtrip():
    m = gp.GenPayload0096(tag='t', score=11)
    d = m.model_dump()
    m2 = gp.GenPayload0096.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 11

def test_gen_payload_0099_roundtrip():
    m = gp.GenPayload0099(tag='t', score=14)
    d = m.model_dump()
    m2 = gp.GenPayload0099.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 14

def test_gen_payload_0102_roundtrip():
    m = gp.GenPayload0102(tag='t', score=0)
    d = m.model_dump()
    m2 = gp.GenPayload0102.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 0

def test_gen_payload_0105_roundtrip():
    m = gp.GenPayload0105(tag='t', score=3)
    d = m.model_dump()
    m2 = gp.GenPayload0105.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 3

def test_gen_payload_0108_roundtrip():
    m = gp.GenPayload0108(tag='t', score=6)
    d = m.model_dump()
    m2 = gp.GenPayload0108.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 6

def test_gen_payload_0111_roundtrip():
    m = gp.GenPayload0111(tag='t', score=9)
    d = m.model_dump()
    m2 = gp.GenPayload0111.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 9

def test_gen_payload_0114_roundtrip():
    m = gp.GenPayload0114(tag='t', score=12)
    d = m.model_dump()
    m2 = gp.GenPayload0114.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 12

def test_gen_payload_0117_roundtrip():
    m = gp.GenPayload0117(tag='t', score=15)
    d = m.model_dump()
    m2 = gp.GenPayload0117.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 15

def test_gen_payload_0120_roundtrip():
    m = gp.GenPayload0120(tag='t', score=1)
    d = m.model_dump()
    m2 = gp.GenPayload0120.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 1

def test_gen_payload_0123_roundtrip():
    m = gp.GenPayload0123(tag='t', score=4)
    d = m.model_dump()
    m2 = gp.GenPayload0123.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 4

def test_gen_payload_0126_roundtrip():
    m = gp.GenPayload0126(tag='t', score=7)
    d = m.model_dump()
    m2 = gp.GenPayload0126.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 7

def test_gen_payload_0129_roundtrip():
    m = gp.GenPayload0129(tag='t', score=10)
    d = m.model_dump()
    m2 = gp.GenPayload0129.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 10

def test_gen_payload_0132_roundtrip():
    m = gp.GenPayload0132(tag='t', score=13)
    d = m.model_dump()
    m2 = gp.GenPayload0132.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 13

def test_gen_payload_0135_roundtrip():
    m = gp.GenPayload0135(tag='t', score=16)
    d = m.model_dump()
    m2 = gp.GenPayload0135.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 16

def test_gen_payload_0138_roundtrip():
    m = gp.GenPayload0138(tag='t', score=2)
    d = m.model_dump()
    m2 = gp.GenPayload0138.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 2

def test_gen_payload_0141_roundtrip():
    m = gp.GenPayload0141(tag='t', score=5)
    d = m.model_dump()
    m2 = gp.GenPayload0141.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 5

def test_gen_payload_0144_roundtrip():
    m = gp.GenPayload0144(tag='t', score=8)
    d = m.model_dump()
    m2 = gp.GenPayload0144.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 8

def test_gen_payload_0147_roundtrip():
    m = gp.GenPayload0147(tag='t', score=11)
    d = m.model_dump()
    m2 = gp.GenPayload0147.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 11

def test_gen_payload_0150_roundtrip():
    m = gp.GenPayload0150(tag='t', score=14)
    d = m.model_dump()
    m2 = gp.GenPayload0150.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 14

def test_gen_payload_0153_roundtrip():
    m = gp.GenPayload0153(tag='t', score=0)
    d = m.model_dump()
    m2 = gp.GenPayload0153.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 0

def test_gen_payload_0156_roundtrip():
    m = gp.GenPayload0156(tag='t', score=3)
    d = m.model_dump()
    m2 = gp.GenPayload0156.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 3

def test_gen_payload_0159_roundtrip():
    m = gp.GenPayload0159(tag='t', score=6)
    d = m.model_dump()
    m2 = gp.GenPayload0159.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 6

def test_gen_payload_0162_roundtrip():
    m = gp.GenPayload0162(tag='t', score=9)
    d = m.model_dump()
    m2 = gp.GenPayload0162.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 9

def test_gen_payload_0165_roundtrip():
    m = gp.GenPayload0165(tag='t', score=12)
    d = m.model_dump()
    m2 = gp.GenPayload0165.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 12

def test_gen_payload_0168_roundtrip():
    m = gp.GenPayload0168(tag='t', score=15)
    d = m.model_dump()
    m2 = gp.GenPayload0168.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 15

def test_gen_payload_0171_roundtrip():
    m = gp.GenPayload0171(tag='t', score=1)
    d = m.model_dump()
    m2 = gp.GenPayload0171.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 1

def test_gen_payload_0174_roundtrip():
    m = gp.GenPayload0174(tag='t', score=4)
    d = m.model_dump()
    m2 = gp.GenPayload0174.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 4

def test_gen_payload_0177_roundtrip():
    m = gp.GenPayload0177(tag='t', score=7)
    d = m.model_dump()
    m2 = gp.GenPayload0177.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 7

def test_gen_payload_0180_roundtrip():
    m = gp.GenPayload0180(tag='t', score=10)
    d = m.model_dump()
    m2 = gp.GenPayload0180.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 10

def test_gen_payload_0183_roundtrip():
    m = gp.GenPayload0183(tag='t', score=13)
    d = m.model_dump()
    m2 = gp.GenPayload0183.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 13

def test_gen_payload_0186_roundtrip():
    m = gp.GenPayload0186(tag='t', score=16)
    d = m.model_dump()
    m2 = gp.GenPayload0186.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 16

def test_gen_payload_0189_roundtrip():
    m = gp.GenPayload0189(tag='t', score=2)
    d = m.model_dump()
    m2 = gp.GenPayload0189.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 2

def test_gen_payload_0192_roundtrip():
    m = gp.GenPayload0192(tag='t', score=5)
    d = m.model_dump()
    m2 = gp.GenPayload0192.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 5

def test_gen_payload_0195_roundtrip():
    m = gp.GenPayload0195(tag='t', score=8)
    d = m.model_dump()
    m2 = gp.GenPayload0195.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 8

def test_gen_payload_0198_roundtrip():
    m = gp.GenPayload0198(tag='t', score=11)
    d = m.model_dump()
    m2 = gp.GenPayload0198.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 11

def test_gen_payload_0201_roundtrip():
    m = gp.GenPayload0201(tag='t', score=14)
    d = m.model_dump()
    m2 = gp.GenPayload0201.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 14

def test_gen_payload_0204_roundtrip():
    m = gp.GenPayload0204(tag='t', score=0)
    d = m.model_dump()
    m2 = gp.GenPayload0204.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 0

def test_gen_payload_0207_roundtrip():
    m = gp.GenPayload0207(tag='t', score=3)
    d = m.model_dump()
    m2 = gp.GenPayload0207.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 3

def test_gen_payload_0210_roundtrip():
    m = gp.GenPayload0210(tag='t', score=6)
    d = m.model_dump()
    m2 = gp.GenPayload0210.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 6

def test_gen_payload_0213_roundtrip():
    m = gp.GenPayload0213(tag='t', score=9)
    d = m.model_dump()
    m2 = gp.GenPayload0213.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 9

def test_gen_payload_0216_roundtrip():
    m = gp.GenPayload0216(tag='t', score=12)
    d = m.model_dump()
    m2 = gp.GenPayload0216.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 12

def test_gen_payload_0219_roundtrip():
    m = gp.GenPayload0219(tag='t', score=15)
    d = m.model_dump()
    m2 = gp.GenPayload0219.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 15

def test_gen_payload_0222_roundtrip():
    m = gp.GenPayload0222(tag='t', score=1)
    d = m.model_dump()
    m2 = gp.GenPayload0222.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 1

def test_gen_payload_0225_roundtrip():
    m = gp.GenPayload0225(tag='t', score=4)
    d = m.model_dump()
    m2 = gp.GenPayload0225.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 4

def test_gen_payload_0228_roundtrip():
    m = gp.GenPayload0228(tag='t', score=7)
    d = m.model_dump()
    m2 = gp.GenPayload0228.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 7

def test_gen_payload_0231_roundtrip():
    m = gp.GenPayload0231(tag='t', score=10)
    d = m.model_dump()
    m2 = gp.GenPayload0231.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 10

def test_gen_payload_0234_roundtrip():
    m = gp.GenPayload0234(tag='t', score=13)
    d = m.model_dump()
    m2 = gp.GenPayload0234.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 13

def test_gen_payload_0237_roundtrip():
    m = gp.GenPayload0237(tag='t', score=16)
    d = m.model_dump()
    m2 = gp.GenPayload0237.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 16

def test_gen_payload_0240_roundtrip():
    m = gp.GenPayload0240(tag='t', score=2)
    d = m.model_dump()
    m2 = gp.GenPayload0240.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 2

def test_gen_payload_0243_roundtrip():
    m = gp.GenPayload0243(tag='t', score=5)
    d = m.model_dump()
    m2 = gp.GenPayload0243.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 5

def test_gen_payload_0246_roundtrip():
    m = gp.GenPayload0246(tag='t', score=8)
    d = m.model_dump()
    m2 = gp.GenPayload0246.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 8

def test_gen_payload_0249_roundtrip():
    m = gp.GenPayload0249(tag='t', score=11)
    d = m.model_dump()
    m2 = gp.GenPayload0249.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 11

def test_gen_payload_0252_roundtrip():
    m = gp.GenPayload0252(tag='t', score=14)
    d = m.model_dump()
    m2 = gp.GenPayload0252.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 14

def test_gen_payload_0255_roundtrip():
    m = gp.GenPayload0255(tag='t', score=0)
    d = m.model_dump()
    m2 = gp.GenPayload0255.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 0

def test_gen_payload_0258_roundtrip():
    m = gp.GenPayload0258(tag='t', score=3)
    d = m.model_dump()
    m2 = gp.GenPayload0258.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 3

def test_gen_payload_0261_roundtrip():
    m = gp.GenPayload0261(tag='t', score=6)
    d = m.model_dump()
    m2 = gp.GenPayload0261.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 6

def test_gen_payload_0264_roundtrip():
    m = gp.GenPayload0264(tag='t', score=9)
    d = m.model_dump()
    m2 = gp.GenPayload0264.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 9

def test_gen_payload_0267_roundtrip():
    m = gp.GenPayload0267(tag='t', score=12)
    d = m.model_dump()
    m2 = gp.GenPayload0267.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 12

def test_gen_payload_0270_roundtrip():
    m = gp.GenPayload0270(tag='t', score=15)
    d = m.model_dump()
    m2 = gp.GenPayload0270.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 15

def test_gen_payload_0273_roundtrip():
    m = gp.GenPayload0273(tag='t', score=1)
    d = m.model_dump()
    m2 = gp.GenPayload0273.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 1

def test_gen_payload_0276_roundtrip():
    m = gp.GenPayload0276(tag='t', score=4)
    d = m.model_dump()
    m2 = gp.GenPayload0276.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 4

def test_gen_payload_0279_roundtrip():
    m = gp.GenPayload0279(tag='t', score=7)
    d = m.model_dump()
    m2 = gp.GenPayload0279.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 7

def test_gen_payload_0282_roundtrip():
    m = gp.GenPayload0282(tag='t', score=10)
    d = m.model_dump()
    m2 = gp.GenPayload0282.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 10

def test_gen_payload_0285_roundtrip():
    m = gp.GenPayload0285(tag='t', score=13)
    d = m.model_dump()
    m2 = gp.GenPayload0285.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 13

def test_gen_payload_0288_roundtrip():
    m = gp.GenPayload0288(tag='t', score=16)
    d = m.model_dump()
    m2 = gp.GenPayload0288.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 16

def test_gen_payload_0291_roundtrip():
    m = gp.GenPayload0291(tag='t', score=2)
    d = m.model_dump()
    m2 = gp.GenPayload0291.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 2

def test_gen_payload_0294_roundtrip():
    m = gp.GenPayload0294(tag='t', score=5)
    d = m.model_dump()
    m2 = gp.GenPayload0294.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 5

def test_gen_payload_0297_roundtrip():
    m = gp.GenPayload0297(tag='t', score=8)
    d = m.model_dump()
    m2 = gp.GenPayload0297.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 8

def test_gen_payload_0300_roundtrip():
    m = gp.GenPayload0300(tag='t', score=11)
    d = m.model_dump()
    m2 = gp.GenPayload0300.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 11

def test_gen_payload_0303_roundtrip():
    m = gp.GenPayload0303(tag='t', score=14)
    d = m.model_dump()
    m2 = gp.GenPayload0303.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 14

def test_gen_payload_0306_roundtrip():
    m = gp.GenPayload0306(tag='t', score=0)
    d = m.model_dump()
    m2 = gp.GenPayload0306.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 0

def test_gen_payload_0309_roundtrip():
    m = gp.GenPayload0309(tag='t', score=3)
    d = m.model_dump()
    m2 = gp.GenPayload0309.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 3

def test_gen_payload_0312_roundtrip():
    m = gp.GenPayload0312(tag='t', score=6)
    d = m.model_dump()
    m2 = gp.GenPayload0312.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 6

def test_gen_payload_0315_roundtrip():
    m = gp.GenPayload0315(tag='t', score=9)
    d = m.model_dump()
    m2 = gp.GenPayload0315.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 9

def test_gen_payload_0318_roundtrip():
    m = gp.GenPayload0318(tag='t', score=12)
    d = m.model_dump()
    m2 = gp.GenPayload0318.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 12

def test_gen_payload_0321_roundtrip():
    m = gp.GenPayload0321(tag='t', score=15)
    d = m.model_dump()
    m2 = gp.GenPayload0321.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 15

def test_gen_payload_0324_roundtrip():
    m = gp.GenPayload0324(tag='t', score=1)
    d = m.model_dump()
    m2 = gp.GenPayload0324.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 1

def test_gen_payload_0327_roundtrip():
    m = gp.GenPayload0327(tag='t', score=4)
    d = m.model_dump()
    m2 = gp.GenPayload0327.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 4

def test_gen_payload_0330_roundtrip():
    m = gp.GenPayload0330(tag='t', score=7)
    d = m.model_dump()
    m2 = gp.GenPayload0330.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 7

def test_gen_payload_0333_roundtrip():
    m = gp.GenPayload0333(tag='t', score=10)
    d = m.model_dump()
    m2 = gp.GenPayload0333.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 10

def test_gen_payload_0336_roundtrip():
    m = gp.GenPayload0336(tag='t', score=13)
    d = m.model_dump()
    m2 = gp.GenPayload0336.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 13

def test_gen_payload_0339_roundtrip():
    m = gp.GenPayload0339(tag='t', score=16)
    d = m.model_dump()
    m2 = gp.GenPayload0339.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 16

def test_gen_payload_0342_roundtrip():
    m = gp.GenPayload0342(tag='t', score=2)
    d = m.model_dump()
    m2 = gp.GenPayload0342.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 2

def test_gen_payload_0345_roundtrip():
    m = gp.GenPayload0345(tag='t', score=5)
    d = m.model_dump()
    m2 = gp.GenPayload0345.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 5

def test_gen_payload_0348_roundtrip():
    m = gp.GenPayload0348(tag='t', score=8)
    d = m.model_dump()
    m2 = gp.GenPayload0348.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 8

def test_gen_payload_0351_roundtrip():
    m = gp.GenPayload0351(tag='t', score=11)
    d = m.model_dump()
    m2 = gp.GenPayload0351.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 11

def test_gen_payload_0354_roundtrip():
    m = gp.GenPayload0354(tag='t', score=14)
    d = m.model_dump()
    m2 = gp.GenPayload0354.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 14

def test_gen_payload_0357_roundtrip():
    m = gp.GenPayload0357(tag='t', score=0)
    d = m.model_dump()
    m2 = gp.GenPayload0357.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 0

def test_gen_payload_0360_roundtrip():
    m = gp.GenPayload0360(tag='t', score=3)
    d = m.model_dump()
    m2 = gp.GenPayload0360.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 3

def test_gen_payload_0363_roundtrip():
    m = gp.GenPayload0363(tag='t', score=6)
    d = m.model_dump()
    m2 = gp.GenPayload0363.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 6

def test_gen_payload_0366_roundtrip():
    m = gp.GenPayload0366(tag='t', score=9)
    d = m.model_dump()
    m2 = gp.GenPayload0366.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 9

def test_gen_payload_0369_roundtrip():
    m = gp.GenPayload0369(tag='t', score=12)
    d = m.model_dump()
    m2 = gp.GenPayload0369.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 12

def test_gen_payload_0372_roundtrip():
    m = gp.GenPayload0372(tag='t', score=15)
    d = m.model_dump()
    m2 = gp.GenPayload0372.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 15

def test_gen_payload_0375_roundtrip():
    m = gp.GenPayload0375(tag='t', score=1)
    d = m.model_dump()
    m2 = gp.GenPayload0375.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 1

def test_gen_payload_0378_roundtrip():
    m = gp.GenPayload0378(tag='t', score=4)
    d = m.model_dump()
    m2 = gp.GenPayload0378.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 4

def test_gen_payload_0381_roundtrip():
    m = gp.GenPayload0381(tag='t', score=7)
    d = m.model_dump()
    m2 = gp.GenPayload0381.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 7

def test_gen_payload_0384_roundtrip():
    m = gp.GenPayload0384(tag='t', score=10)
    d = m.model_dump()
    m2 = gp.GenPayload0384.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 10

def test_gen_payload_0387_roundtrip():
    m = gp.GenPayload0387(tag='t', score=13)
    d = m.model_dump()
    m2 = gp.GenPayload0387.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 13

def test_gen_payload_0390_roundtrip():
    m = gp.GenPayload0390(tag='t', score=16)
    d = m.model_dump()
    m2 = gp.GenPayload0390.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 16

def test_gen_payload_0393_roundtrip():
    m = gp.GenPayload0393(tag='t', score=2)
    d = m.model_dump()
    m2 = gp.GenPayload0393.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 2

def test_gen_payload_0396_roundtrip():
    m = gp.GenPayload0396(tag='t', score=5)
    d = m.model_dump()
    m2 = gp.GenPayload0396.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 5

def test_gen_payload_0399_roundtrip():
    m = gp.GenPayload0399(tag='t', score=8)
    d = m.model_dump()
    m2 = gp.GenPayload0399.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 8

def test_gen_payload_0402_roundtrip():
    m = gp.GenPayload0402(tag='t', score=11)
    d = m.model_dump()
    m2 = gp.GenPayload0402.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 11

def test_gen_payload_0405_roundtrip():
    m = gp.GenPayload0405(tag='t', score=14)
    d = m.model_dump()
    m2 = gp.GenPayload0405.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 14

def test_gen_payload_0408_roundtrip():
    m = gp.GenPayload0408(tag='t', score=0)
    d = m.model_dump()
    m2 = gp.GenPayload0408.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 0

def test_gen_payload_0411_roundtrip():
    m = gp.GenPayload0411(tag='t', score=3)
    d = m.model_dump()
    m2 = gp.GenPayload0411.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 3

def test_gen_payload_0414_roundtrip():
    m = gp.GenPayload0414(tag='t', score=6)
    d = m.model_dump()
    m2 = gp.GenPayload0414.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 6

def test_gen_payload_0417_roundtrip():
    m = gp.GenPayload0417(tag='t', score=9)
    d = m.model_dump()
    m2 = gp.GenPayload0417.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 9

def test_gen_payload_0420_roundtrip():
    m = gp.GenPayload0420(tag='t', score=12)
    d = m.model_dump()
    m2 = gp.GenPayload0420.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 12

def test_gen_payload_0423_roundtrip():
    m = gp.GenPayload0423(tag='t', score=15)
    d = m.model_dump()
    m2 = gp.GenPayload0423.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 15

def test_gen_payload_0426_roundtrip():
    m = gp.GenPayload0426(tag='t', score=1)
    d = m.model_dump()
    m2 = gp.GenPayload0426.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 1

def test_gen_payload_0429_roundtrip():
    m = gp.GenPayload0429(tag='t', score=4)
    d = m.model_dump()
    m2 = gp.GenPayload0429.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 4

def test_gen_payload_0432_roundtrip():
    m = gp.GenPayload0432(tag='t', score=7)
    d = m.model_dump()
    m2 = gp.GenPayload0432.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 7

def test_gen_payload_0435_roundtrip():
    m = gp.GenPayload0435(tag='t', score=10)
    d = m.model_dump()
    m2 = gp.GenPayload0435.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 10

def test_gen_payload_0438_roundtrip():
    m = gp.GenPayload0438(tag='t', score=13)
    d = m.model_dump()
    m2 = gp.GenPayload0438.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 13

def test_gen_payload_0441_roundtrip():
    m = gp.GenPayload0441(tag='t', score=16)
    d = m.model_dump()
    m2 = gp.GenPayload0441.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 16

def test_gen_payload_0444_roundtrip():
    m = gp.GenPayload0444(tag='t', score=2)
    d = m.model_dump()
    m2 = gp.GenPayload0444.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 2

def test_gen_payload_0447_roundtrip():
    m = gp.GenPayload0447(tag='t', score=5)
    d = m.model_dump()
    m2 = gp.GenPayload0447.model_validate(d)
    assert m2.tag == 't'
    assert m2.score == 5

