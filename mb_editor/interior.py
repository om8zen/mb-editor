from mb_editor.sceneobject import SceneObject
from mb_editor.utils import path


class Interior(SceneObject):
    classname = 'InteriorInstance'

    defaults = dict(
        interiorFile=''
    )

    @classmethod
    def local(cls, interiorFile, subdir='', **fields):
        return cls(interiorFile=path.join('~/data/interiors_pq/custom', subdir, interiorFile), **fields)

    @staticmethod
    def tests():
        i = Interior.local('foundationRepair.dif')
        assert i.interiorFile == '~/data/interiors_pq/custom/foundationRepair.dif'


if __name__ == '__main__':
    Interior.tests()
