import stripe


stripe.api_key = 'sk_test_51I8iATIqXYelWJBByYQUj7VUiZEQN8bqB21s3Mr1wtaCrD3bkIu5zIXp08MecUfzrPORzz4FS0nj1jYoIEg0n6NZ004Gb29U5r'

intent = stripe.PaymentIntent.create(
  amount=1099,
  currency='inr',
  # Verify your integration in this guide by including this parameter
  metadata={'integration_check': 'accept_a_payment'},
)