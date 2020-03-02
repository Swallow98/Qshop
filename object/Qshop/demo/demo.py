# 支付宝支付
from alipay import AliPay

alipay_public_key_string= """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAkeRiprRv1aub5rxrzxptGlGgIZy8qPpsVr1c9+27T+w1Cvbvzehc6SVc43EwPEWYWzGxV9dHrOFw4eqnZ6wYIobNll2ERx+Wub3y+AMRk1h1631Cp1ybg+/zRWGILpPTvmaXU7b8Xka+CJY/t2FXq77Esfj4f5Qt++GEU/BDpMFV+pFkluQKkq1ntcuP8wXmft8eL0/RYwff3VWPo0+MWi8ChOGcducl9LJ9PUQLiJpGVZWpzwDI9KPK2E+l5v3Q+LLnyrREhHXMdPv+o1qArlq9hnctwBr6zQAVRkrfD9/mu09ueTlFy7ZRH4TPnyiURvSwP2WAzYpb7u5KtzWEgwIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCR5GKmtG/Vq5vmvGvPGm0aUaAhnLyo+mxWvVz37btP7DUK9u/N6FzpJVzjcTA8RZhbMbFX10es4XDh6qdnrBgihs2WXYRHH5a5vfL4AxGTWHXrfUKnXJuD7/NFYYguk9O+ZpdTtvxeRr4Ilj+3YVervsSx+Ph/lC374YRT8EOkwVX6kWSW5AqSrWe1y4/zBeZ+3x4vT9FjB9/dVY+jT4xaLwKE4Zx25yX0sn09RAuImkZVlanPAMj0o8rYT6Xm/dD4sufKtESEdcx0+/6jWoCuWr2Gdy3AGvrNABVGSt8P3+a7T255OUXLtlEfhM+fKJRG9LA/ZYDNilvu7kq3NYSDAgMBAAECggEAXffgosdtkQ6rp/6M4iR/SYhxv7SYv64sweHOU9LH5z6ZG6rZ4qJb1b+/CLALBYc+Dt7+/zkmbW/3qUve76OlF/gDy2oInVb3WkPCj4RKecFsknVnzSyU7nJLGtErSfTlWanypnUiMAcYt6cu+wqz0Wdagdd/F4114NrsxLPoneD6RNwKW5aXCZQdOCT5HQ/sTnB0rP8xdzuSef3pB+YGvzBb0KEvpi083d+8Wnj2oU4Y6DhhmI/S84tchr3JYqElsiWGGytLnZbIPvCNApxoDX3uSoa3NuUV8CN8++8MVJVIs15CLzhmy+fE0Y+D1VNoiGKxHvbVgyNN241FwrRzwQKBgQDxUtrad5uQPFUacL8OFJw9g0veMd3/2nYeGWtlqCuNLSzFjrdhwlsoGRZZSQgjBwFngfTOamefrwnvYvqLVv8wOCqyWOKbREhiEHU+ELrd2i+REOdlUPdFW2yK6Y+2CAM+bFpwRUeOZZ3AeDmTfZNsIAaOfIV5Lc4rpmC42OoNewKBgQCaw8QhCV83aDRPO6v5nuXOi3jWeyDzMIdpk34MvRGd9vEkVUz9dNaweoYTceKU7APJ2m/qpVXraqE1CECOWIY7IzI1+V30l51huNHhkcQUlvPRK/SKzsn4tH80fZnmd7VHMprpZ4a/mKjNPkCmVG7dm2AvrPIZd10vrxMhEQGCmQKBgDjuaA0kLIIBib48HQaQXC+y2uInd40Vl8oQCyMnYmbi4m4U9jRM6r5x9LDJpu7Eh1NI+Fz+A0ZLwBdGjX7z3i4dAg2jJIqmuEDSSyaCQeN2xsP9bemcCUnGgLvgz/OMvl8qpsdXwMLaPDYc5tBhzrayc3mH7OEiqkHn9WeGXOkjAoGANT8td4BV9iYv+SK6pIN65Xku9fwe9gy4Siaos5FJQmP3y1xdxMYyJz3Aa2g/YKVjGEvDPaPsz7Y8CJbyPwdOB4Kwf8lv/fs79qcz7rvMDplxAYJx/F/xNVREf7bHAHgnMnvCuJMZ1UmcqiDE9XUPP8d5bG3ATeq3cPR3TGUhc+ECgYEAvuBuAK3DQ/MfmvI6tGitq11wnPZW0zvX9yeiQm0e9YpTQuFQvAORwY/g+nS1pXSGvSK0YGVbv/vJwolFrjndtgBUW7NAGZe4guxNLJBoC9Eb/Xp2pIszYf9+1AcZRAbl0fsyyqR8+3Lw6hAM5BBw283x+v0hJ3finK5hb2DvJpI=
 -----END RSA PRIVATE KEY-----"""

# 实例化对象
alipay = AliPay(
    appid='2016101800717525',
    app_notify_url=None,
    app_private_key_string=app_private_key_string,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",
    debug=False
)

# 实例化一个订单
order_string = alipay.api_alipay_trade_page_pay(
    subject='水果交易',
    out_trade_no='1234567876543',
    total_amount='999.99',
    return_url=None,
    notify_url=None
)

#
result = 'https://openapi.alipaydev.com/gateway.do?' + order_string
print(result)

