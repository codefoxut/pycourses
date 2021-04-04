"""Module for motion detection through webcam."""

import cv2
import time
import pandas
from datetime import datetime
from bokeh.plotting import figure, output_file, show
from bokeh.models import HoverTool, ColumnDataSource


def plotting_motion():
    df = make_df()

    df["start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
    df["end_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

    df.to_csv("Times.csv")

    cds = ColumnDataSource(df)

    p = figure(x_axis_type='datetime', height=100, width=500, title="Motion Graph")
    p.yaxis.minor_tick_line_color = None
    # p.ygrid.ticker.desired_num_ticks = 1

    hover = HoverTool(tooltips=[("Start", "@start_string"), ("End", "@end_string")])
    p.add_tools(hover)

    q = p.quad(left="Start", right="End", bottom=0, top=1, color="green", source=cds)

    print(q)
    output_file("Graph.html")
    show(p)


def make_df():
    df = pandas.DataFrame(columns=["Start", "End"])
    times = capture_video()

    for i in range(0, len(times), 2):
        df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)
    return df


def capture_video():
    first_frame = None
    status_list = [None, 0]
    times = []
    video = cv2.VideoCapture(0)

    while True:
        check, frame = video.read()

        status = 0

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if first_frame is None:
            first_frame = gray
            cv2.imshow("First frame", first_frame)
            continue

        # get delta from first frame
        delta_frame = cv2.absdiff(first_frame, gray)
        # make binary image with a threshold
        thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

        (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue

            status = 1
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

        status_list.append(status)

        if status_list[-1] == 1 and status_list[-2] == 0:
            times.append(datetime.now())
        if status_list[-1] == 0 and status_list[-2] == 1:
            times.append(datetime.now())

        status_list = status_list[-2:]

        # time.sleep()
        cv2.imshow("Capturing", gray)
        cv2.imshow("Delta Frame", delta_frame)
        cv2.imshow("Threshold Frame", thresh_frame)
        cv2.imshow("COLOR frame", frame)

        key = cv2.waitKey(1)
        # print(gray)
        # print(thresh_frame)

        if key == ord('q'):
            if status == 1:
                times.append(datetime.now())
            break

        print(status)

    print(status_list)
    print(times)
    video.release()
    cv2.destroyAllWindows()
    return times


if __name__ == '__main__':
    # capture_video()
    # df1 = make_df()
    # df1.to_csv("Times.csv")
    plotting_motion()
