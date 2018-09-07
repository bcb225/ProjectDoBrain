interface RootObject {
    todayMissionChapterButtonIndexes: number[];
    dateTimeForWeek: string;
    weekClearMissionCount: number;
    dateTimeForMonth: string;
    todayClearMissionCount: number;
    kidsLabWeekData: KidsLabWeekDatum[];
    monthClearMissionCount: number;
    monthTotalMissionCount: number;
    updateDateTime: string;
    dateTimeForToday: string;
  }
  
  interface KidsLabWeekDatum {
    velocityPerceptualPoint: number;
    memoryPoint: number;
    organizingPoint: number;
    startDateTime: string;
    creativePoint: number;
    weekIndex: number;
    spacePerceptualPoint: number;
    numericalPoint: number;
    discriminationPoint: number;
    inferencePoint: number;
  }