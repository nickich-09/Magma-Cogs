from .request import request


async def setup(bot):
    await bot.add_cog(request(bot))
