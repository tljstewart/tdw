# automatically generated by the FlatBuffers compiler, do not modify

# namespace: FBOutput

import tdw.flatbuffers

class ArrivedAtNavMeshDestination(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsArrivedAtNavMeshDestination(cls, buf, offset):
        n = tdw.flatbuffers.encode.Get(tdw.flatbuffers.packer.uoffset, buf, offset)
        x = ArrivedAtNavMeshDestination()
        x.Init(buf, n + offset)
        return x

    # ArrivedAtNavMeshDestination
    def Init(self, buf, pos):
        self._tab = tdw.flatbuffers.table.Table(buf, pos)

    # ArrivedAtNavMeshDestination
    def AvatarId(self):
        o = tdw.flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def ArrivedAtNavMeshDestinationStart(builder): builder.StartObject(1)
def ArrivedAtNavMeshDestinationAddAvatarId(builder, avatarId): builder.PrependUOffsetTRelativeSlot(0, tdw.flatbuffers.number_types.UOffsetTFlags.py_type(avatarId), 0)
def ArrivedAtNavMeshDestinationEnd(builder): return builder.EndObject()