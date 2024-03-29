import json
import numpy

__all__ = ['json_encode']


def json_encode(data):
    class MyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, numpy.integer):
                return int(obj)
            elif isinstance(obj, numpy.floating):
                return float(obj)
            elif isinstance(obj, numpy.ndarray):
                return obj.tolist()
            else:
                return super(MyEncoder, self).default(obj)

    return json.dumps(data, cls=MyEncoder)
