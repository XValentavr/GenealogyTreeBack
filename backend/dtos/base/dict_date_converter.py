from pydantic import BaseModel


class DictDateConverterMixin(BaseModel):

    def dict(self, **kwargs):
        d = super().dict(**kwargs)
        d['date'] = d['date'].date()
        return d
