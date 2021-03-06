import discord

def get_text_from_file(filename):
    with open(filename,'r') as fp:
        return fp.read()

def create_embed(ctx,*args,**kwargs):
    embed = discord.Embed(title=kwargs['title'])
    for field in kwargs['fields']:
        embed.add_field(name=field['name'],value=field['value'], inline=True)
    formated_time = ctx.message.created_at.strftime("%H:%M %b %d %Y")
    embed.set_footer(text=f'Requested by {ctx.message.author.name} at {formated_time}')
    return embed