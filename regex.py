import twitter

api=twitter.Api(consumer_key='saCDWX1qDubugy3bcyIFAl7q1',
                consumer_secret='zacBFtxhFwsyY16Z8tQNKMSxTvATX0XomiVtG8sVy484W5DeaR',
				access_token_key='236541800-mbFTzDuX7fintCdsjoLmyiqxOFFTJoFczICSddFx',
				access_token_secret='rSXJ7T03rS8s841tDB6TaEjdLyH6MCfGCtLRJ2ymbU2oq')
print(api.VerifyCredentials())