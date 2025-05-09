d_output = (y - output) * dsigmoid(output)
    # d_hidden = d_output.dot(wout.T) * dsigmoid(hlayer)

    # wout += hlayer.T.dot(d_output) * lr
    # wh += X.dot(d_hidden) * lr