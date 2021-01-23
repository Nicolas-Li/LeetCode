class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        if T == 0:
            return 0
        clips.sort(key=lambda clip: clip[0] * 1000 + clip[1])
        clips.append([101, 101])
        dest = 0 # 最长剪辑长度
        nex = 0
        step  = 0
        for clip in clips:
            if dest >= clip[0]:
                nex = max([clip[1], nex])
            else:
                dest = nex
                step += 1
                nex = max([clip[1], nex]) if dest >= clip[0] else nex
                if dest >= T:
                    break
        return step if dest >= T else -1
                
